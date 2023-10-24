
from os import environ

from .localhost import *  # noqa: F403

########## DATABASE CONFIGURATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "{{ cookiecutter.database_name }}",
        "USER": "postgres",
        "PASSWORD": "localhost",
        "HOST": environ["DB_HOST"],
        "PORT": "5432",
    },
}
########## END DATABASE CONFIGURATION

if DEBUG:  # noqa: F405
    import socket  # only if you haven't already imported this

    _, __, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = (
        *(ip[: ip.rfind(".")] + ".1" for ip in ips),
        "10.0.2.2",
        *INTERNAL_IPS,  # noqa: F405
    )

EMAIL_HOST = "mail"

########## QUEUE CONFIGURATION
CELERY_BROKER_URL = "redis://redis:6379/1"
########## END QUEUE CONFIGURATION

########## CACHE CONFIGURATION
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PARSER_CLASS": "redis.connection._HiredisParser",
        },
        "TIMEOUT": 24 * 60 * 60,
        "VERSION": 1,
    },
}

DJANGO_REDIS_IGNORE_EXCEPTIONS = True
DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True
DJANGO_REDIS_LOGGER = f"{LOG_ROOT}.{__name__}"  # noqa: F405
########## END CACHE CONFIGURATION
