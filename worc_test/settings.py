from pathlib import Path
from datetime import timedelta

import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-n1jk3b_!qe+sykpoecoslw+5)bky_c2q*)$@waihbm2a@29f-h"

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # My Apps
    "worc_test.apps.accounts",
    "worc_test.apps.candidates",
    "worc_test.apps.reports",
    "cpf_field",
    "drf_yasg",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "worc_test.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "worc_test.wsgi.application"


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
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


# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=20),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(days=10),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=20),
}

LOGGING = {
    "version": 1,
    "loggers": {"django": {"handlers": ["file", "file2"], "level": "DEBUG"}},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "./logs/info.log",
            "formatter": "simpleRe",
        },
        "file2": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "./logs/debug.log",
            "formatter": "simpleRe",
        },
        "file3": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "./logs/warning.log",
            "formatter": "simpleRe",
        },
        "file4": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "./logs/error.log",
            "formatter": "simpleRe",
        },
        "file5": {
            "level": "FATAL",
            "class": "logging.FileHandler",
            "filename": "./logs/fatal.log",
            "formatter": "simpleRe",
        },
    },
    "formatters": {
        "simpleRe": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        }
    },
}


SWAGGER_SETTINGS = {
    "REFETCH_SCHEMA_WITH_AUTH": True,
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
    "APIS_SORTER": "alpha",
    "DOC_EXPANSION": None,
    "SHOW_REQUEST_HEADERS": True,
    "SUPPORTED_SUBMIT_METHODS": ["get", "post", "put", "delete", "patch"],
    "OPERATIONS_SORTER": "alpha",
    "LOGIN_URL": "/login/",
    "LOGOUT_URL": "/logout/",
}

django_heroku.settings(locals())
