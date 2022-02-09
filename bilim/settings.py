"""
Django settings for app project.
Generated by 'django-admin startproject' using Django 3.2.3.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from kombu import Queue
from celery.schedules import crontab
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['185.100.67.153']
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('ALLOWED_HOSTS', '').split(','),
    )
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Project modules
    'core',
    'authorize',
    'school',
    'university',
    'student',
    'tasker',
    'juicy',
    # REQUIREMENTS
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'celery'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
]

ROOT_URLCONF = 'bilim.urls'

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

WSGI_APPLICATION = 'bilim.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}
# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'authorize.services.auth_token.TokenAuthenticationCustom',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'authorize.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = '/vol/web/static'

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
    'http://185.100.67.153',
    "http://127.0.0.1:3000"
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ['*']

CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"
CELERY_BEAT_SCHEDULE = {
    "sample_task": {
        "task": "bilim.tasks.sample_task",
        "schedule": crontab(minute="*/1"),
    },
    "chain_trek": {
        "task": "bilim.tasks.chain_trek",
        "schedule": timedelta(seconds=15)
    },
    "group_trek": {
        "task": "bilim.tasks.group_trek",
        "schedule": timedelta(seconds=10)
    },
    "car_add": {
        "task": "bilim.tasks.car_add",
        "schedule": crontab(minute="*/1"),
    },
}
# 
# CELERY_IGNORE_RESULT = True
# CELERY_DEFAULT_QUEUE = 'default'
# CELERY_DEFAULT_HIGH = 'high'
# CELERY_QUEUES = (
#     Queue('default', routing_key='default'),
#     Queue('high', routing_key='high'),
# )
# CELERY_ROUTES = {
#     # -- HIGH PRIORITY QUEUE -- #
#     'authorize.tasks.user_mail': {'queue': 'high'},
#     # 'Operation.tasks.email_send_check_pdf': {'queue': 'high'},
#     # 'Operation.tasks.email_z_report': {'queue': 'high'},
#     # 'Operation.tasks.one_day_shift': {'queue': 'high'},
#     # 'Place.tasks.auto_closin_shift_task': {'queue': 'high'},
#     # -- DEFAULT QUEUE -- #
#     # 'Place.tasks.check_blocking': {'queue': 'default'},
#     # 'Place.tasks.offline_mode': {'queue': 'default'},
#     # 'Place.tasks.send_offline': {'queue': 'default'},
#     # 'Server.tasks.graylogging': {'queue': 'default'},
# }
# CELERYD_PREFETCH_MULTIPLIER = os.environ.get('CELERYD_PREFETCH_MULTIPLIER')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL CONFIG
# -----------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USER_NAME = 'Beket Samaluly'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "djangobeket@gmail.com"
EMAIL_HOST_PASSWORD = "djangobek587"
