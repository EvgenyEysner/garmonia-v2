# Garmonia v2

Marketing website and content-management backend for **Kosmetikstudio Garmonia / Schoenheitsecke Oldenburg**, a beauty salon in Oldenburg, Germany.

The project is a decoupled web application: a statically generated Vue 3 single-page site for visitors and a Django REST API that serves the salon's content (services, prices, gallery, testimonials, monthly offers) and handles contact requests. Everything is shipped as a Docker Compose stack behind an Nginx reverse proxy with automated TLS, and it coexists on the same server with a separate Mailcow mail stack.

Production domain: `https://schoenheitsecke-oldenburg.de`

---

## Table of contents

- [Architecture](#architecture)
- [Repository layout](#repository-layout)
- [Technology stack](#technology-stack)
- [Local development](#local-development)
- [Environment variables](#environment-variables)
- [Running with Docker Compose](#running-with-docker-compose)
- [Nginx and TLS](#nginx-and-tls)
- [Mailcow integration](#mailcow-integration)
- [Deployment](#deployment)
- [Testing](#testing)
- [Component documentation](#component-documentation)

---

## Architecture

```
                              Internet
                                 |
                    ports 80 / 443 (HTTP/HTTPS)
                                 |
                       +---------------------+
                       |   nginx (container) |  reverse proxy + TLS termination
                       +----------+----------+
                                  |
          +-----------------------+------------------------+
          |                       |                        |
   /  (static site)        /api/, /admin/            mail.* (proxy)
          |                       |                        |
   +------v------+         +------v------+          host.docker.internal:8443
   |  frontend   |         |   backend   |                 |
   | (Vue SSG +  |         | (Django +   |          +------v---------+
   |  nginx)     |         |  Gunicorn)  |          | Mailcow stack  |
   +-------------+         +------+------+          | (separate)     |
                                  |                 +----------------+
                           +------v------+
                           | PostgreSQL  |
                           +-------------+

   certbot (container)  ->  shared Let's Encrypt volume  ->  nginx
```

- The **frontend** is pre-rendered to static HTML (vite-ssg) and served by a small Nginx inside its own container.
- The **backend** exposes a JSON REST API under `/api/` and the Django admin under `/admin/`.
- The top-level **nginx** container terminates TLS, serves `/static/` and `/media/`, proxies `/api/` and `/admin/` to the backend, proxies everything else to the frontend, and reverse-proxies the `mail.*` subdomain to the host's Mailcow Nginx.
- **certbot** renews Let's Encrypt certificates into a shared volume; nginx reloads periodically to pick up new certificates.

---

## Repository layout

```
garmonia-v2/
├── backend/                 Django project (REST API, admin, business logic)
│   ├── accounts/            Custom user model and authentication
│   ├── app/                 Domain app: models, serializers, views, tests
│   ├── config/              Django settings, URLs, WSGI/ASGI
│   ├── mailcow/scripts/     Helper scripts for Mailcow certificate handling
│   ├── scripts/             Container entrypoints (run_backend.sh, migrations.sh)
│   ├── Dockerfile
│   ├── pyproject.toml       Python dependencies (managed with uv)
│   └── README.md
├── frontend/                Vue 3 + Vite single-page application
│   ├── src/                 Components, views, router, services, content
│   ├── public/              robots.txt, sitemap.xml, icons, OG images
│   ├── docs/                Frontend setup notes (SSG)
│   ├── Dockerfile
│   ├── nginx.conf           Static file server config for the frontend image
│   ├── package.json
│   └── README.md
├── nginx/                   Reverse proxy configuration
│   ├── nginx.conf           Main site (always required)
│   ├── conf.d/              Optional vHosts (e.g. mail.conf)
│   └── proxy_params         Shared proxy headers
├── docker-compose.yml       Production stack definition
├── .env.production.example  Template for production environment variables
└── README.md                This file
```

---

## Technology stack

| Layer            | Technology                                                        |
| ---------------- | ----------------------------------------------------------------- |
| Frontend         | Vue 3, TypeScript, Vite 7, vite-ssg, Tailwind CSS 4, Pinia, Vue Router, Axios, Leaflet |
| Backend          | Python 3.12, Django 6, Django REST Framework, SimpleJWT, drf-spectacular, django-unfold |
| Database         | PostgreSQL 17                                                      |
| Email            | Resend (transactional email for the contact form)                 |
| Web server       | Nginx (reverse proxy and static file serving)                     |
| TLS              | Let's Encrypt via Certbot                                          |
| Mail server      | Mailcow (runs as a separate stack on the same host)               |
| Containerization | Docker, Docker Compose                                             |
| CI/CD            | GitHub Actions (SSH deploy on push to `master`)                   |

---

## Local development

Each part can be run independently for development. See the dedicated READMEs for full instructions:

- Backend: [`backend/README.md`](backend/README.md)
- Frontend: [`frontend/README.md`](frontend/README.md)

Quick start (two terminals):

```bash
# Terminal 1 - backend (requires a local PostgreSQL and a backend .env)
cd backend
uv sync
uv run python manage.py migrate
uv run python manage.py runserver 0.0.0.0:8000

# Terminal 2 - frontend
cd frontend
npm install
npm run dev
```

The frontend dev server runs on `http://localhost:5173` and talks to the API at the URL defined by `VITE_API_BASE_URL`.

---

## Environment variables

The backend reads a single `.env` file from the repository root (see `environ.Env.read_env` in `backend/config/settings.py`). Copy the template and fill in real values:

```bash
cp .env.production.example .env
```

Backend variables:

| Variable                      | Description                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| `SECRET_KEY`                  | Django secret key                                            |
| `DEBUG`                       | `True` for development, `False` in production                |
| `ALLOWED_HOSTS`               | Comma-separated host names                                   |
| `CSRF_TRUSTED_ORIGINS`        | Comma-separated origins (production)                         |
| `CORS_ALLOWED_ORIGINS`        | Comma-separated origins allowed to call the API             |
| `DATABASE_USER`               | PostgreSQL user                                              |
| `DATABASE_PASSWORD`           | PostgreSQL password                                          |
| `DATABASE_NAME`               | PostgreSQL database name                                     |
| `DATABASE_HOST`               | Database host (`db` inside Compose)                          |
| `DATABASE_PORT`               | Database port (default `5432`)                               |
| `DJANGO_STATIC_ROOT`          | Path/name for collected static files                        |
| `DJANGO_SESSION_COOKIE_SECURE`| `True` in production                                         |
| `DJANGO_SECURE_HSTS_SECONDS`  | HSTS max-age in seconds (e.g. `31536000`)                    |
| `API_DOCS_ENABLED`            | Exposes `/api/schema/*` when `True` (default `False`)        |
| `RESEND_API_KEY`              | Resend API key for the contact form                         |
| `RESEND_FROM_EMAIL`           | Verified sender address                                      |
| `RECIPIENT_ADDRESS`           | Where contact requests are delivered                        |
| `RESEND_TIMEOUT`              | Request timeout for Resend (seconds)                         |

Frontend variables (`frontend/.env`, baked in at build time):

| Variable                | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| `VITE_API_BASE_URL`     | Base URL of the backend API                            |
| `VITE_STUDIO_LOCATION`  | Latitude,longitude used by the Leaflet map             |
| `VITE_GA4_ID`           | Google Analytics 4 measurement ID                      |

Do not commit `.env` files that contain secrets. Only `.env.production.example` is tracked.

---

## Running with Docker Compose

The production stack is defined in `docker-compose.yml` and uses the Compose project name `garmonia` (this fixes volume names such as `garmonia_certbot-etc`, which the Mailcow scripts rely on).

```bash
# Build and start the full stack
docker compose build
docker compose up -d

# Watch backend logs (collectstatic + Gunicorn)
docker compose logs -f backend

# Run database migrations manually if needed
docker compose run --rm backend python manage.py migrate

# Create an admin user
docker compose run --rm backend python manage.py createsuperuser
```

Services:

| Service    | Description                                            | Exposed |
| ---------- | ------------------------------------------------------ | ------- |
| `db`       | PostgreSQL 17                                           | internal |
| `backend`  | Django + Gunicorn (runs collectstatic on start)        | internal `:8000` |
| `frontend` | Pre-rendered Vue site served by Nginx                  | internal `:80` |
| `nginx`    | Reverse proxy and TLS termination                      | `80`, `443` |
| `certbot`  | Automatic Let's Encrypt renewal loop                   | internal |

Named volumes: `garmonia-db` (database), `media` (uploads), `staticfiles` (collected static), `certbot-etc` and `certbot-www` (TLS).

---

## Nginx and TLS

- `nginx/nginx.conf` contains the always-required configuration for the main website (HTTP to HTTPS redirect, ACME challenge, `/static/`, `/media/`, `/api/`, `/admin/`, SPA proxy, security headers, rate limiting).
- `nginx/conf.d/*.conf` holds optional virtual hosts. Each optional vHost lives in its own file so that a missing certificate only affects that single host, not the whole server.
- `nginx/conf.d/mail.conf` reverse-proxies `mail.schoenheitsecke-oldenburg.de` to the host's Mailcow Nginx.

To temporarily disable an optional vHost (for example before its certificate exists):

```bash
mv nginx/conf.d/mail.conf nginx/conf.d/mail.conf.disabled
docker compose exec nginx nginx -s reload
```

Certificates are stored in the shared `certbot-etc` volume. The `certbot` container renews them automatically; the `nginx` container reloads every six hours so renewed certificates are picked up without manual intervention.

---

## Mailcow integration

Mailcow runs as a **separate** Docker Compose stack on the same host (it is not part of this repository's stack). The integration points are:

- The top-level Nginx reverse-proxies the `mail.*` subdomain to Mailcow's internal Nginx on `host.docker.internal:8443`.
- Mailcow's own Let's Encrypt is disabled; the certificate for the mail subdomain is issued by this project's Certbot and synced into Mailcow.

Helper scripts live in `backend/mailcow/scripts/`:

- `issue-cert.sh` issues the initial certificate for the mail subdomain via the webroot challenge.
- `sync-letsencrypt.sh` copies the renewed certificate into the Mailcow stack and reloads the relevant Mailcow services. It is idempotent and safe to run on a schedule.

---

## Deployment

Deployment is automated with GitHub Actions (`.github/workflows/deploy.yaml`). On every push to `master`, the workflow connects to the server over SSH and runs:

```bash
cd /home/www/garmonia
git pull <repo> master
docker compose build
docker compose up -d
docker compose exec -T nginx nginx -t
docker compose exec -T nginx nginx -s reload
```

Required GitHub repository secrets: `SERVER_HOST`, `SERVER_USER`, `SSH_PRIVATE_KEY`, `GH_TOKEN`.

For a manual deploy, run the same commands on the server. Always ensure `.env` exists on the server with production values before starting the stack.

---

## Testing

Backend tests use Django's test runner and require the database service:

```bash
docker compose up -d db
docker compose run --rm backend python manage.py test
```

The suite covers the public API endpoints (categories, treatments, monthly offers, gallery, testimonials), the contact endpoint (validation, success, throttling, mail-provider failure) and the email service.

---

## Component documentation

- [`backend/README.md`](backend/README.md) - Django API, data model, commands, deployment details.
- [`frontend/README.md`](frontend/README.md) - Vue application, build, SSG, analytics and consent.
- [`frontend/docs/SSG-SETUP.md`](frontend/docs/SSG-SETUP.md) - Static site generation notes.
