import structlog

from os import environ
from envparse import env
from .base import *

env.read_envfile()

########## HOST CONFIGURATION
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
########## END HOST CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME", default=""),
        "USER": env.str("DB_USER", default=""),
        "PASSWORD": env.str("DB_PASSWORD", default=""),
        "HOST": env.str("DB_HOST", default=""),
        "PORT": "5432",
    }
}
########## END DATABASE CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "settings.wsgi.production.application"
########## END WSGI CONFIGURATION


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
