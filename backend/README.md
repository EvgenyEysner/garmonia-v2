# Garmonia Backend

Django REST API and content-management backend for the Garmonia / Schoenheitsecke Oldenburg website. It serves the salon's public content (categories, treatments, monthly offers, gallery, testimonials), handles contact-form submissions via Resend, and provides a styled Django admin for editing content.

This service is the source of truth for all dynamic data consumed by the [frontend](../frontend/README.md).

---

## Table of contents

- [Technology stack](#technology-stack)
- [Project structure](#project-structure)
- [Data model](#data-model)
- [API reference](#api-reference)
- [Authentication](#authentication)
- [Local setup](#local-setup)
- [Environment variables](#environment-variables)
- [Database migrations](#database-migrations)
- [Running tests](#running-tests)
- [Admin interface](#admin-interface)
- [Email (contact form)](#email-contact-form)
- [Production notes](#production-notes)

---

## Technology stack

- Python 3.12
- Django 6
- Django REST Framework
- djangorestframework-simplejwt (JWT authentication)
- drf-spectacular (OpenAPI schema and Swagger/Redoc, optional)
- django-unfold (admin theme)
- django-cors-headers, django-filter
- PostgreSQL 17 (via psycopg2)
- Gunicorn (production WSGI server)
- Resend (transactional email)
- uv (dependency management)

---

## Project structure

```
backend/
├── accounts/                Custom user model and manager
│   ├── models.py            CustomUser (email login)
│   ├── managers.py          UserManager
│   └── migrations/
├── app/                     Domain application
│   ├── models.py            Category, Treatment, MonthlyOffer, Testimonial, GalleryImage
│   ├── serializers.py       DRF serializers for each model + contact payload
│   ├── views.py             ViewSets and the contact endpoint
│   ├── routers.py           DRF router registrations
│   ├── admin.py             Unfold-based admin configuration
│   ├── services/email.py    Resend integration
│   ├── migrations/
│   └── tests/               API and service tests
├── config/                  Django project configuration
│   ├── settings.py          Settings (env-driven)
│   ├── urls.py              URL routing
│   ├── wsgi.py / asgi.py
├── mailcow/scripts/         Mailcow certificate helper scripts
├── scripts/                 Container entrypoints
│   ├── run_backend.sh       Production: collectstatic + Gunicorn
│   ├── run_backend_local.sh Development: migrate + runserver
│   └── migrations.sh        Apply migrations only
├── Dockerfile
└── pyproject.toml
```

---

## Data model

All content models live in `app/models.py`. The user model lives in `accounts/models.py`.

| Model          | Key fields                                                        | Notes                                              |
| -------------- | ----------------------------------------------------------------- | -------------------------------------------------- |
| `Category`     | `name`                                                            | Groups treatments                                  |
| `Treatment`    | `name`, `category` (FK), `description`, `price`                   | `price` is free text (e.g. "ab 60") up to 20 chars |
| `MonthlyOffer` | `treatment` (FK), `title`, `description`, `image`, `active`, `price` | Only `active=True` offers are exposed by the API   |
| `Testimonial`  | `first_name`, `last_name`, `text`, `rating`                      | `rating` is validated to be between 1 and 5         |
| `GalleryImage` | `image`, `description`                                            | Uploaded to `media/gallery/`                        |
| `CustomUser`   | `email`, `first_name`, `last_name`, `is_staff`, `is_active`       | Email is the login field (`USERNAME_FIELD`)         |

Uploaded files:

- Monthly offer images: `media/offers/`
- Gallery images: `media/gallery/`

---

## API reference

Base path: `/api/`

| Method | Endpoint                | Description                                            | Auth |
| ------ | ----------------------- | ------------------------------------------------------ | ---- |
| GET    | `/api/category/`        | List all categories (unpaginated)                      | none |
| GET    | `/api/treatment/`       | List all treatments with nested category (unpaginated) | none |
| GET    | `/api/monthly-offer/`   | List active monthly offers (unpaginated)               | none |
| GET    | `/api/gallery/`         | Up to 9 random gallery images                          | none |
| GET    | `/api/testimonial/`     | Up to 6 random testimonials                            | none |
| POST   | `/api/contact/`         | Submit a contact request (sends an email)              | none, throttled |

Administration and documentation:

| Endpoint                  | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| `/admin/`                 | Django admin (Unfold theme)                            |
| `/api/schema/`            | OpenAPI schema (only when `API_DOCS_ENABLED=True`)     |
| `/api/schema/swagger/`    | Swagger UI (only when `API_DOCS_ENABLED=True`)         |
| `/api/schema/redoc/`      | Redoc UI (only when `API_DOCS_ENABLED=True`)           |

### Contact endpoint

`POST /api/contact/`

Request body:

```json
{
  "name": "Max Mustermann",
  "email": "max@example.com",
  "phone": "+49 179 123456",
  "treatment_id": 1,
  "message": "Termin am Freitag bitte"
}
```

Responses:

- `201 Created` - request accepted and email dispatched.
- `400 Bad Request` - validation failed (missing fields or unknown `treatment_id`).
- `429 Too Many Requests` - throttle limit exceeded (5 requests per hour per client).
- `503 Service Unavailable` - the email provider rejected or could not be reached.

---

## Authentication

The public content and contact endpoints are open (`AllowAny`). The project ships with SimpleJWT configured (short-lived access tokens, rotating refresh tokens, blacklist after rotation) for future authenticated features and for securing the admin. There are currently no public login endpoints; admin access is via the Django admin session login.

---

## Local setup

Prerequisites: Python 3.12, [uv](https://docs.astral.sh/uv/), and a running PostgreSQL instance.

```bash
cd backend

# Install dependencies into a virtual environment
uv sync

# Provide environment variables (the project reads ../.env relative to backend/)
cp ../.env.production.example ../.env   # then edit for local values

# Apply migrations
uv run python manage.py migrate

# Create an admin user
uv run python manage.py createsuperuser

# Start the development server
uv run python manage.py runserver 0.0.0.0:8000
```

The API is then available at `http://localhost:8000/api/` and the admin at `http://localhost:8000/admin/`.

For a local setup that mirrors production more closely, use Docker Compose from the repository root (see the root README).

---

## Environment variables

Settings are env-driven (`config/settings.py`) and loaded from a `.env` file located one level above `backend/` (the repository root).

| Variable                       | Required | Description                                           |
| ------------------------------ | -------- | ----------------------------------------------------- |
| `SECRET_KEY`                   | yes      | Django secret key                                     |
| `DEBUG`                        | yes      | `True` / `False`                                      |
| `ALLOWED_HOSTS`                | yes      | Comma-separated host names                            |
| `DATABASE_USER`                | yes      | PostgreSQL user                                       |
| `DATABASE_PASSWORD`            | yes      | PostgreSQL password                                   |
| `DATABASE_NAME`                | yes      | PostgreSQL database                                   |
| `DATABASE_HOST`                | yes      | Database host                                         |
| `DATABASE_PORT`                | yes      | Database port                                         |
| `DJANGO_STATIC_ROOT`           | yes      | Target for `collectstatic`                            |
| `DJANGO_SESSION_COOKIE_SECURE` | yes      | Secure cookies (`True` in production)                 |
| `DJANGO_SECURE_HSTS_SECONDS`   | no       | HSTS max-age (default `0`)                            |
| `CSRF_TRUSTED_ORIGINS`         | prod     | Comma-separated trusted origins                       |
| `CORS_ALLOWED_ORIGINS`         | no       | Comma-separated allowed API origins                   |
| `API_DOCS_ENABLED`             | no       | Expose schema/Swagger/Redoc (default `False`)         |
| `RESEND_API_KEY`               | for mail | Resend API key                                        |
| `RESEND_FROM_EMAIL`            | for mail | Verified sender address                               |
| `RECIPIENT_ADDRESS`            | no       | Contact recipient (has a default)                     |
| `RESEND_TIMEOUT`               | no       | Resend request timeout in seconds (default `15`)      |

Security-related settings (`SECURE_SSL_REDIRECT`, `CSRF_COOKIE_SECURE`) derive from `DJANGO_SESSION_COOKIE_SECURE`, and `SECURE_PROXY_SSL_HEADER` is set so Django trusts the `X-Forwarded-Proto` header from Nginx.

---

## Database migrations

```bash
# Create migrations after model changes
uv run python manage.py makemigrations

# Apply migrations
uv run python manage.py migrate

# Verify the models and migrations are in sync
uv run python manage.py makemigrations --check --dry-run
```

Inside Docker Compose:

```bash
docker compose run --rm backend python manage.py migrate
```

---

## Running tests

Tests require a PostgreSQL database. With Docker Compose:

```bash
docker compose up -d db
docker compose run --rm backend python manage.py test
```

Locally with uv (against a reachable database):

```bash
uv run python manage.py test
```

Test coverage includes:

- `app/tests/test_api_category.py` - category listing and response shape
- `app/tests/test_api_treatment.py` - treatment listing
- `app/tests/test_api_monthly_offer.py` - only active offers are returned
- `app/tests/test_api_gallery.py` - gallery sampling
- `app/tests/test_api_testimonial.py` - testimonial sampling
- `app/tests/test_api_contact.py` - validation, success, throttling (429), provider failure (503)
- `app/tests/test_send_email_service.py` - Resend integration

---

## Admin interface

The admin uses django-unfold for a themed UI matching the salon's branding. Registered models: `Category`, `Treatment`, `MonthlyOffer`, `Testimonial`, `GalleryImage`. The gallery admin renders image thumbnails.

Access at `/admin/`. Create a superuser with `createsuperuser`.

---

## Email (contact form)

Contact submissions are delivered with [Resend](https://resend.com). The integration lives in `app/services/email.py`:

- Requires `RESEND_API_KEY` and `RESEND_FROM_EMAIL`.
- Sends a plain-text email to `RECIPIENT_ADDRESS` summarizing the request.
- Sets `reply_to` to the visitor's email so replies go directly to them.
- Raises `ResendError` on misconfiguration or provider failure, which the view translates into a `503` response.

The endpoint is throttled to 5 requests per hour per client (DRF `ScopedRateThrottle`, scope `contact`).

---

## Production notes

In production the backend runs via `scripts/run_backend.sh`, which executes `collectstatic` and then starts Gunicorn:

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 1800 --graceful-timeout 1800
```

The container exposes port `8000` internally; the top-level Nginx proxies `/api/` and `/admin/` to it and serves `/static/` and `/media/` directly from shared volumes. See the [root README](../README.md) for the full stack and deployment workflow.
