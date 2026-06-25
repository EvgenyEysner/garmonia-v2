#!/usr/bin/env bash
# import-existing-certs.sh
# ----------------------------------------------------------------------
# Imports existing Let's Encrypt certificates from the host filesystem
# into the Garmonia Docker certbot volume (garmonia_certbot-etc).
#
# Use when migrating from a standalone certbot/nginx setup on the same
# server — avoids re-issuing certs and hitting Let's Encrypt rate limits.
#
# Run on the server as root or with docker group, BEFORE starting nginx
# if certs are not yet in the volume:
#   sudo ./scripts/import-existing-certs.sh
#   docker compose up -d
# ----------------------------------------------------------------------

set -euo pipefail

GARMONIA_DIR="${GARMONIA_DIR:-/home/www/garmonia}"
HOST_LETSENCRYPT="${HOST_LETSENCRYPT:-/etc/letsencrypt}"
GARMONIA_PROJECT="${GARMONIA_PROJECT:-garmonia}"
CERTBOT_VOLUME="${GARMONIA_PROJECT}_certbot-etc"

DOMAINS=(
  "schoenheitsecke-oldenburg.de"
  "mail.schoenheitsecke-oldenburg.de"
)

log() { printf '[import-certs] %s\n' "$*"; }

if [[ ! -d "$HOST_LETSENCRYPT/live" ]]; then
  log "ERROR: $HOST_LETSENCRYPT/live not found on host"
  exit 1
fi

cd "$GARMONIA_DIR"

docker volume inspect "$CERTBOT_VOLUME" >/dev/null 2>&1 || docker volume create "$CERTBOT_VOLUME"

for domain in "${DOMAINS[@]}"; do
  if [[ ! -d "$HOST_LETSENCRYPT/live/$domain" ]]; then
    log "SKIP: no host cert for $domain"
    continue
  fi

  log "Importing $domain from $HOST_LETSENCRYPT ..."
  docker run --rm \
    -v "${CERTBOT_VOLUME}:/etc/letsencrypt" \
    -v "${HOST_LETSENCRYPT}:/host-le:ro" \
    alpine:3.20 \
    sh -ce "
      mkdir -p /etc/letsencrypt/live/$domain
      cp -aL /host-le/live/$domain/. /etc/letsencrypt/live/$domain/
      if [ -d /host-le/archive/$domain ]; then
        mkdir -p /etc/letsencrypt/archive/$domain
        cp -a /host-le/archive/$domain/. /etc/letsencrypt/archive/$domain/
      fi
      if [ -f /host-le/renewal/${domain}.conf ]; then
        mkdir -p /etc/letsencrypt/renewal
        cp /host-le/renewal/${domain}.conf /etc/letsencrypt/renewal/
      fi
    "
  log "OK: $domain"
done

log "Verify inside nginx container:"
log "  docker compose exec nginx ls -la /etc/letsencrypt/live/"
log ""
log "If mail.* was imported, sync to Mailcow:"
log "  sudo backend/mailcow/scripts/sync-letsencrypt.sh"
log ""
log "Optional — disable host certbot timer to avoid double renewal:"
log "  sudo systemctl disable --now certbot.timer  # if using systemd certbot on host"
