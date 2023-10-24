import structlog

from os import environ
from django.http import request

from .base import *

# STATIC_ROOT is required to run collectstatic locally.
STATIC_ROOT = normpath(join(SITE_ROOT, "interfaces/assets"))  # type: ignore

# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # type: ignore
########## END DEBUG CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "{{ cookiecutter.python_package_name }}.settings.wsgi.localhost.application"
########## END WSGI CONFIGURATION


########## HOST CONFIGURATION
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]
########## END HOST CONFIGURATION


########## SESSION CONFIGRATION
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
########## END DEBUG CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "{{ cookiecutter.database_name }}",
        "USER": "postgres",
        "PASSWORD": "localhost",
        "HOST": environ.get("DB_HOST", "localhost"),
        "PORT": "5432",
    }
}
########## END DATABASE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (  # type: ignore
    "debug_toolbar",
    "django_extensions",
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ("127.0.0.1",)
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Force enable the toolbar in docker container
def show_toolbar(request: request.HttpRequest) -> bool:
    return DEBUG is False

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "{{ cookiecutter.python_package_name }}.settings.configuration.localhost.show_toolbar",
}
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE += (  # type: ignore
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)
########## END TOOLBAR CONFIGURATION


########## CORS CONFIGURATION
# See: https://github.com/ottoyiu/django-cors-headers/
CORS_ORIGIN_ALLOW_ALL = True
########## END CORS CONFIGURATION


########## PASSWORD HASHERS CONFIGURATION
# Enable weaker but faster algorithms
PASSWORD_HASHERS = (  # type: ignore
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
)
########## END PASSWORD HASHERS CONFIGURATION


########## LOGGING CONFIGURATION
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "formatters": {
        "simple": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "{{ cookiecutter.python_package_name }}": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "celery": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## EMAIL CONFIGURATION
EMAIL_HOST = "mail"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAILS_PER_SECOND = 80
########## END EMAIL CONFIGURATION


########## QUEUE CONFIGURATION
BROKER_URL = "amqp://guest:guest@rabbitmq:5672/"
########## END QUEUE CONFIGURATION
