"""
Django settings for cdui project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os

import oracledb

from config.env import BASE_DIR, env

env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('DJANGO_SECRET_KEY', os.getenv('DJANGO_SECRET_KEY', 'SECRET'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# oracledb.init_oracle_client()

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cruise'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF = 'cdui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'cruise_database': {
        "ENGINE": "django.db.backends.oracle",
        "NAME": os.getenv('ORACLE_DB_NAME'),
        "USER": os.getenv('ORACLE_DB_USER'),
        "PASSWORD": os.getenv('ORACLE_DB_PASS'),
        "HOST": os.getenv('ORACLE_DB_HOST'),
        "PORT": os.getenv('ORACLE_DB_PORT', 1521),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOG_DIRECTORY = env.str('LOG_DIRECTORY', os.getenv('LOG_DIRECTORY', 'logs'))

if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)

FORMATTERS = (
    {
        "simple": {
            "format": "{levelname} {asctime:s} {module} {filename} {lineno:d} {funcName} - {message}",
            "style": "{"
        },
        "verbose": {
            "format": "{levelname} {asctime:s} {threadName} {thread:d} {module} {filename} {lineno:d} {name} "
                      "{funcName} {process:d} - {message}",
            "style": "{"
        },
    },
)

HANDLERS = {
    "console": {
        "class": "logging.StreamHandler",
        "formatter": "simple",
    },
    "file_handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": os.path.join(LOG_DIRECTORY, 'info.log'),
        "mode": "a",
        "encoding": "utf-8",
        "formatter": "verbose",
        "backupCount": 5,
        "maxBytes": 1024 * 1024 * 2  # 2 MB
    }
}

LOGGERS = (
    {
        "django": {
            "handlers": ["console", "file_handler"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ['file_handler'],
            "level": "ERROR",
            "propagate": True,
        },
        "cdui": {
            "handlers": ["console", "file_handler"],
            "level": "DEBUG",
            "propagate": True
        },
    },
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": FORMATTERS[0],
    "handlers": HANDLERS,
    "loggers": LOGGERS[0],
}