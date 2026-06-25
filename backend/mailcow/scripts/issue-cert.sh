#!/usr/bin/env bash
# issue-cert.sh
# ----------------------------------------------------------------------
# One-shot: stellt das initiale Let's-Encrypt-Zertifikat für die Mailcow-
# Subdomain via webroot-Challenge des bestehenden Garmonia-Certbot aus.
#
# Voraussetzungen:
#   - DNS A/AAAA-Record für $DOMAIN zeigt auf diesen Server
#   - Garmonia-Stack läuft, nginx ist erreichbar auf Port 80
#   - nginx.conf enthält bereits den HTTP-Block mit
#     `location /.well-known/acme-challenge/` für $DOMAIN
# ----------------------------------------------------------------------

set -euo pipefail

DOMAIN="${DOMAIN:-mail.schoenheitsecke-oldenburg.de}"
EMAIL="${EMAIL:-postmaster@schoenheitsecke-oldenburg.de}"
GARMONIA_DIR="${GARMONIA_DIR:-/home/www/garmonia}"

cd "$GARMONIA_DIR"

echo "[issue-cert] Stellt Cert aus für $DOMAIN (E-Mail: $EMAIL)"
docker compose run --rm --entrypoint "" certbot \
  certbot certonly \
    --webroot \
    --webroot-path=/var/www/certbot \
    --email "$EMAIL" \
    --agree-tos --no-eff-email \
    --rsa-key-size 4096 \
    -d "$DOMAIN"

echo "[issue-cert] Reload Garmonia-nginx"
docker compose exec nginx nginx -t
docker compose exec nginx nginx -s reload

echo "[issue-cert] Done. Jetzt: sudo /usr/local/sbin/mailcow-cert-sync"
