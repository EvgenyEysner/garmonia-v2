import os
from datetime import timedelta
from pathlib import Path

# https://django-environ.readthedocs.io/en/latest/getting-started.html#installation
import environ
from corsheaders.defaults import default_methods
from django.templatetags.static import static

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# --- Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, "../.env"))

SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

AUTH_USER_MODEL = "accounts.CustomUser"

INSTALLED_APPS = (
    # --- django unfold
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # needs for full-text search with postgres
    "django.contrib.postgres",
)

LOCAL_APPS = ("accounts", "app")
THIRD_PARTY_APPS = (
    "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular",
    "django_extensions",
    "rest_framework",
    "corsheaders",
    "django_filters",
)

INSTALLED_APPS += LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
    }
}

UNFOLD = {
    "SITE_TITLE": "Webseite Verwaltung",
    "SITE_DROPDOWN": [
        {
            "icon": "diamond",
            "title": "Garmonia Kosmetikstudio",
            "link": "https://schoenheitsecke-oldenburg.de",
        },
    ],
    "SITE_URL": "https://schoenheitsecke-oldenburg.de",
    "SITE_LOGO": {
        "light": lambda request: static("image/garmonia_logo_neu.webp"),
        "dark": lambda request: static("image/garmonia_logo_neu.webp"),
    },
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_BACK_BUTTON": False,
    "THEME": "light",
    "LOGIN": {
        "image": lambda request: static("image/home-header.webp"),
    },
    "BORDER_RADIUS": "6px",
    "COLORS": {
        # Sand (Sekundär) – frontend --color-sand-*
        "base": {
            "50": "#fafaf9",
            "100": "#f5f5f4",
            "200": "#e7e5e4",
            "300": "#d6d3d1",
            "400": "#a8a29e",
            "500": "#78716c",
            "600": "#57534e",
            "700": "#44403c",
            "800": "#292524",
            "900": "#1c1917",
            "950": "#0c0a09",
        },
        # Gold (Primär) – frontend --color-gold-*
        "primary": {
            "50": "#faf7f2",
            "100": "#f5ede0",
            "200": "#ead9c0",
            "300": "#dfc5a0",
            "400": "#d4a373",
            "500": "#c49363",
            "600": "#b38353",
            "700": "#8f6942",
            "800": "#6b4f32",
            "900": "#473521",
            "950": "#2a1f14",
        },
        # Textfarben – frontend body, nav, placeholders
        "font": {
            "subtle-light": "#78716c",
            "subtle-dark": "#a8a29e",
            "default-light": "#44403c",
            "default-dark": "#d6d3d1",
            "important-light": "#1c1917",
            "important-dark": "#f5f5f4",
        },
    },
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "PAGE_SIZE": 100,
    # --- To enable filtering, search and ordering in DRF ---------------- #
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    # Rate limiting setting that restricts access Telegram Login View.
    # It prevents a client from sending too many requests in a short period of time.
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.ScopedRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "contact": "5/hour",  # Spam protection for contact form submissions
    },
}

SPECTECULAR_SETTINGS = {
    "TITLE": "Garmonia API",
    "DESCRIPTION": "Garmonia API Documentation",
    "VERSION": "0.0.0",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=30),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "VERIFYING_KEY": SECRET_KEY,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SIGNING_KEY": SECRET_KEY,
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE")
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=0)
if SECURE_HSTS_SECONDS > 0:
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# --- Security middleware settings ------------------------------------------------ #
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = SESSION_COOKIE_SECURE

# --- Use X-Forwarded-Proto Header to determine SSL status (useful for API docs) --- #
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# --- Csrf middleware settings ------------------------------------------------------ #
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE

# --- Referrer-Policy middleware ---------------------------------------------------- #
REFERRER_POLICY = "same-origin"
API_DOCS_ENABLED = env.bool("API_DOCS_ENABLED", default=False)

if DEBUG:
    CSRF_TRUSTED_ORIGINS = [
        "http://127.0.0.1:8000",
        "http://localhost:8000",
        "http://127.0.0.1",
        "http://localhost",
    ]
else:
    CSRF_TRUSTED_ORIGINS = env.list(
        "CSRF_TRUSTED_ORIGINS",
        default=["https://schoenheitsecke-oldenburg.de"],
    )
CSRF_USE_SESSIONS = True

CORS_ALLOW_CREDENTIALS = True
CORS_URLS_REGEX = "/api/.*"

CORS_ALLOW_METHODS = default_methods

CORS_ALLOWED_ORIGINS = env.list(
    "CORS_ALLOWED_ORIGINS",
    default=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://schoenheitsecke-oldenburg.de",
        "https://www.schoenheitsecke-oldenburg.de",
    ],
)

# --- CSP Config ----------------------------------------- #
CSP_DEFAULT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "https://stats.g.doubleclick.net",
    "https://www.googletagmanager.com",
    "https://region1.google-analytics.com",
)

CSP_CONNECT_SRC = (
    "'self'",
    "https://stats.g.doubleclick.net",
    "https://region1.google-analytics.com",  # Analytics-Domain
    "https://www.googletagmanager.com",  # Optional, if Tag Manager establishes connections
    "http://localhost:8000",  # For local development environments
)

CSP_IMG_SRC = (
    "'self'",
    "data:",
    "https://www.google.de",
    "https://stats.g.doubleclick.net",
    "https://region1.google-analytics.com",
    "https://www.googletagmanager.com",
)

CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "https://www.googletagmanager.com",
    "https://www.google-analytics.com",
)

LANGUAGE_CODE = "de-de"
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_TZ = True

# --- Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = env("DJANGO_STATIC_ROOT")
STATICFILES_DIRS = ("static/",)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- E-Mail (Resend) ----------------------------------- #
RESEND_API_KEY = env("RESEND_API_KEY", default="")
RESEND_FROM_EMAIL = env("RESEND_FROM_EMAIL", default="")
RECIPIENT_ADDRESS = env("RECIPIENT_ADDRESS", default="garmonia.eisner@gmail.com")
RESEND_TIMEOUT = env.int("RESEND_TIMEOUT", default=15)
