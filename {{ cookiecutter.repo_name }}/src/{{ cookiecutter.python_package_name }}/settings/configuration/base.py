import os
from datetime import timedelta
from os.path import dirname, join, normpath
from typing import List, Collection

########## PATH CONFIGURATION
# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(dirname(os.path.dirname(__file__)))
# Absolute filesystem path to the top-level test folder:
TEST_ROOT = dirname(SITE_ROOT) + "/tests"
########## END PATH CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = f"{{ cookiecutter.python_package_name }}.interfaces.urls"
########## END URL CONFIGURATION


########## SESSION CONFIGRATION
SESSION_COOKIE_AGE = 2419200
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "Lax"
JWT_AUTH = {
    "JWT_VERIFY_EXPIRATION": False,
    "JWT_EXPIRATION_DELTA": timedelta(days=7),
}
########## END DEBUG CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("Administrator", ""),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = "UTC"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "ja"
# for intcomma
NUMBER_GROUPING = 3

LANGUAGES = (
    ("ja", "Japanese"),
)

LOCALE_PATHS = [f"{SITE_ROOT}/locale/"]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## LOGIN CONFIGURATION
LOGIN_URL = "/login/"
########## END LOGIN CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, "interfaces/static")),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)
FAVICON_PATH = f"{STATIC_URL}img/common/favicon.ico"
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"^z(!&%ys=q*6&!7ibdvscl&)wag*(l1cgbt(u#!l-^vsyj7#l2"
########## END SECRET CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
ALLOWED_HOSTS = []  # type: List[str]
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(TEST_ROOT, "fixtures")),
)
########## END FIXTURE CONFIGURATION


########## EMAIL BACKEND CONFIGURATION
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
########## END EMAIL BACKEND CONFIGURATION

# Avoid writing too much data to the session storage by using CookieStorage.
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"


########## TEMPLATE CONFIGURATION
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            normpath(join(SITE_ROOT, "interfaces/templates")),
        ],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
            "loaders": [
                ("django.template.loaders.cached.Loader", (
                    "django.template.loaders.filesystem.Loader",
                    "django.template.loaders.app_directories.Loader",
                )),
            ],
            "debug": DEBUG
        },
    },
]
# https://github.com/gregmuellegger/django-mobile/issues/72
TEMPLATE_LOADERS = TEMPLATES[0]["OPTIONS"]["loaders"]  # type: ignore
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE = (
    ## These Middleware should be defined before CommonMiddleware
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)
########## END MIDDLEWARE CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.humanize",
    # Admin panel and documentation:
    "django.contrib.admin",
    "django.contrib.admindocs",
)

# Apps specific for this project go here.
LOCAL_APPS = (
    "{{ cookiecutter.python_package_name }}.interfaces.accounts.Config",
    "{{ cookiecutter.python_package_name }}.interfaces.authentication.Config",
)

THIRD_PARTY_APPS = ()
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
########## END APP CONFIGURATION


# auth model
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # user and password
    # ModelBackend is the slowest therefore is the last of the list.
)


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        },
    },
}

# defining root of the logging hierarchy. used by getLogger().
LOG_ROOT = "{{ cookiecutter.python_package_name }}"
LOG_STATS_ROOT = "{{ cookiecutter.python_package_name }}.stats"
########## END LOGGING CONFIGURATION


# Raven/Sentry
SENTRY_AUTO_LOG_STACKS = True
#################


########## PASSWORD HASHERS CONFIGURATION
# designate bcrypt as the hashing algorithm to store passwords.
PASSWORD_HASHERS = (
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
)
########## END PASSWORD HASHERS CONFIGURATION


########## CORS CONFIGURATION for API
# See: https://github.com/ottoyiu/django-cors-headers/
CORS_ORIGIN_REGEX_WHITELIST = (
    r"^(https?://)?([\w\-]+\.)?{{ cookiecutter.repo_name }}\.local$",
)
CORS_ALLOW_HEADERS = ("x-requested-with", "content-type", "accept", "origin", "authorization",
                      "x-csrftoken", "cache-control")
CORS_ALLOW_CREDENTIALS = True
########## END CORS CONFIGURATION


########## QUEUE CONFIGURATION
BROKER_URL = ""
########## END QUEUE CONFIGURATION


REDIRECT_HTTPS_DISABLE = False