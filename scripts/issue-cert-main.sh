#!/usr/bin/env bash
# issue-cert-main.sh
# ----------------------------------------------------------------------
# One-shot: initial Let's Encrypt certificate for the main website domain
# via webroot challenge (Garmonia certbot + nginx on port 80).
#
# Prerequisites:
#   - DNS A/AAAA for schoenheitsecke-oldenburg.de (+ www) points to this server
#   - Garmonia stack running; nginx reachable on port 80
#   - No conflicting certbot on the host binding port 80
# ----------------------------------------------------------------------

set -euo pipefail

DOMAIN="${DOMAIN:-schoenheitsecke-oldenburg.de}"
EMAIL="${EMAIL:-moin@schoenheitsecke-oldenburg.de}"
GARMONIA_DIR="${GARMONIA_DIR:-/home/www/garmonia}"

cd "$GARMONIA_DIR"

echo "[issue-cert-main] Requesting cert for $DOMAIN and www.$DOMAIN (email: $EMAIL)"
docker compose run --rm --entrypoint "" certbot \
  certbot certonly \
    --webroot \
    --webroot-path=/var/www/certbot \
    --email "$EMAIL" \
    --agree-tos --no-eff-email \
    --rsa-key-size 4096 \
    -d "$DOMAIN" \
    -d "www.$DOMAIN"

echo "[issue-cert-main] Reload nginx"
docker compose exec nginx nginx -t
docker compose exec nginx nginx -s reload

echo "[issue-cert-main] Done."
