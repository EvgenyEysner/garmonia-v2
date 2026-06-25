#!/usr/bin/env bash
# mailcow-cert-sync
# ----------------------------------------------------------------------
# Kopiert das von der Garmonia-Certbot-Instanz ausgestellte Let's-Encrypt-
# Zertifikat für mail.schoenheitsecke-oldenburg.de in den Mailcow-Stack
# und triggert nur dann einen Reload der relevanten Mailcow-Container,
# wenn sich das Cert tatsächlich geändert hat.
#
# Idempotent — kann gefahrlos im Minutentakt laufen.
#
# Erwartet:
#   - Garmonia-Stack unter $GARMONIA_DIR mit docker-volume "garmonia_certbot-etc"
#   - Mailcow-Stack unter $MAILCOW_DIR
#   - Cert-Live-Pfad unter /etc/letsencrypt/live/$DOMAIN/ im certbot-etc-Volume
# ----------------------------------------------------------------------

set -euo pipefail

DOMAIN="${DOMAIN:-mail.schoenheitsecke-oldenburg.de}"
GARMONIA_DIR="${GARMONIA_DIR:-/home/www/garmonia}"
MAILCOW_DIR="${MAILCOW_DIR:-/home/www/mailcow-dockerized}"
GARMONIA_PROJECT="${GARMONIA_PROJECT:-garmonia}"  # docker compose -p ...; ggf. anpassen
CERTBOT_VOLUME="${GARMONIA_PROJECT}_certbot-etc"

MAILCOW_SSL_DIR="${MAILCOW_DIR}/data/assets/ssl"
TARGET_CERT="${MAILCOW_SSL_DIR}/cert.pem"
TARGET_KEY="${MAILCOW_SSL_DIR}/key.pem"

log() { printf '[mailcow-cert-sync] %s %s\n' "$(date -Is)" "$*"; }

# --- Sanity checks ----------------------------------------------------
if [[ ! -d "$MAILCOW_DIR" ]]; then
  log "ERROR: Mailcow dir '$MAILCOW_DIR' not found"; exit 1
fi
if ! docker volume inspect "$CERTBOT_VOLUME" >/dev/null 2>&1; then
  log "ERROR: docker volume '$CERTBOT_VOLUME' not found"
  log "Hint: 'docker volume ls' to inspect; set GARMONIA_PROJECT to the right name"
  exit 1
fi

mkdir -p "$MAILCOW_SSL_DIR"

# --- Read current cert+key out of the certbot volume ------------------
TMP_CERT="$(mktemp)"; TMP_KEY="$(mktemp)"
trap 'rm -f "$TMP_CERT" "$TMP_KEY"' EXIT

docker run --rm \
  -v "${CERTBOT_VOLUME}:/etc/letsencrypt:ro" \
  alpine:3.20 \
  sh -c "cat /etc/letsencrypt/live/${DOMAIN}/fullchain.pem" > "$TMP_CERT"

docker run --rm \
  -v "${CERTBOT_VOLUME}:/etc/letsencrypt:ro" \
  alpine:3.20 \
  sh -c "cat /etc/letsencrypt/live/${DOMAIN}/privkey.pem" > "$TMP_KEY"

if [[ ! -s "$TMP_CERT" || ! -s "$TMP_KEY" ]]; then
  log "ERROR: Cert oder Key leer — wurde das Zertifikat schon ausgestellt?"
  exit 2
fi

# --- Compare ----------------------------------------------------------
NEW_HASH="$(sha256sum "$TMP_CERT" | awk '{print $1}')"
OLD_HASH=""
if [[ -f "$TARGET_CERT" ]]; then
  OLD_HASH="$(sha256sum "$TARGET_CERT" | awk '{print $1}')"
fi

if [[ "$NEW_HASH" == "$OLD_HASH" ]]; then
  log "Cert unverändert (sha256=$NEW_HASH) — nothing to do."
  exit 0
fi

# --- Install ----------------------------------------------------------
install -m 0644 "$TMP_CERT" "$TARGET_CERT"
install -m 0600 "$TMP_KEY"  "$TARGET_KEY"
log "Cert installed: $TARGET_CERT (sha256=$NEW_HASH)"

# --- Reload Mailcow services that consume the cert --------------------
cd "$MAILCOW_DIR"
# postfix, dovecot, nginx-mailcow lesen das Cert beim Start;
# `restart` ist sicher und kurz (< 5 s)
docker compose restart postfix-mailcow dovecot-mailcow nginx-mailcow
log "Mailcow services reloaded."
