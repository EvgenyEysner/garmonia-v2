import os
from datetime import timedelta

# https://django-environ.readthedocs.io/en/latest/getting-started.html#installation
import environ
from corsheaders.defaults import default_methods

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# --- Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# --- Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, "../.env"))

SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS_LIST = env.list("ALLOWED_HOSTS")

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

LOCAL_APPS = ("accounts", "app", "review")
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
            "title": "Lagerverwaltung",
            "link": "/",
        },
    ],
    "SITE_URL": "/",
    # "SITE_LOGO": {
    #     "light": lambda request: static("image/koenig_logo.png"),
    #     "dark": lambda request: static("image/koenig_logo.png"),
    # },
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_BACK_BUTTON": False,
    "THEME": "dark",
    # "LOGIN": {
    #     "image": lambda request: static("image/admin-bg.jpeg"),
    # },
    # "STYLES": [
    #     lambda request: static("css/style.css"),
    # ],
    # "SCRIPTS": [
    #     lambda request: static("js/script.js"),
    # ],
    "BORDER_RADIUS": "6px",
    "COLORS": {
        # Grau-Blau Basis (angepasst an die grauen Elemente im Logo)
        "base": {
            "50": "oklch(98% .005 240)",
            "100": "oklch(96% .008 240)",
            "200": "oklch(92% .012 240)",
            "300": "oklch(86% .018 240)",
            "400": "oklch(70% .025 240)",
            "500": "oklch(55% .030 240)",
            "600": "oklch(45% .032 240)",
            "700": "oklch(38% .035 240)",
            "800": "oklch(28% .035 240)",
            "900": "oklch(22% .033 240)",
            "950": "oklch(15% .030 240)",
        },
        # Primärfarbe: Dunkelblau aus den Solarpanels
        "accent": {
            "50": "oklch(96% .015 250)",
            "100": "oklch(92% .030 250)",
            "200": "oklch(85% .055 250)",
            "300": "oklch(75% .085 250)",
            "400": "oklch(60% .115 250)",
            "500": "oklch(45% .140 252)",  # Hauptfarbe: Dunkelblau der Panels
            "600": "oklch(38% .145 252)",
            "700": "oklch(32% .140 252)",
            "800": "oklch(26% .130 252)",
            "900": "oklch(22% .110 252)",
            "950": "oklch(16% .090 252)",
        },
        # Akzentfarbe: Gelb/Orange aus Sonne und Blitz
        "primary": {
            "50": "oklch(98% .020 85)",
            "100": "oklch(95% .045 85)",
            "200": "oklch(90% .090 85)",
            "300": "oklch(85% .130 85)",
            "400": "oklch(78% .165 80)",
            "500": "oklch(72% .190 75)",  # Goldgelb der Sonne
            "600": "oklch(65% .180 70)",
            "700": "oklch(55% .160 70)",
            "800": "oklch(45% .140 70)",
            "900": "oklch(35% .110 70)",
            "950": "oklch(25% .080 70)",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",
            "subtle-dark": "var(--color-base-400)",
            "default-light": "var(--color-base-700)",
            "default-dark": "var(--color-base-300)",
            "important-light": "var(--color-base-900)",
            "important-dark": "var(--color-base-100)",
        },
    },
}

REST_FRAMEWORK = {
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
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

CORS_ALLOW_CREDENTIALS = True
CORS_URLS_REGEX = "/api/.*"

CORS_ALLOW_METHODS = default_methods
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    "x-csrftoken",
    "accept",
    "origin",
]

CORS_ALLOWED_ORIGINS = (
    "http://localhost:5173",
    "http://127.0.0.1:5173",
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

# --- Google API ----------------------------------------- #
GOOGLE_CLIENT_ID = env("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = env("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = env("GOOGLE_REDIRECT_URI")
GOOGLE_ACCOUNT_ID = env("GOOGLE_ACCOUNT_ID")
GOOGLE_LOCATION_ID = env("GOOGLE_LOCATION_ID")
