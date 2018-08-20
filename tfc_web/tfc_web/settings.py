"""
Django settings for tfc_web project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from machina import MACHINA_MAIN_TEMPLATE_DIR, MACHINA_MAIN_STATIC_DIR, get_apps as get_machina_apps
from tfc_web.secrets import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['smartcambridge.org', 'www.smartcambridge.org', '.cl.cam.ac.uk', 'localhost', '127.0.0.1', '[::1]']

# Application apps
PROJECT_APPS = [
    'tfc_gis',
    'transport',
    'parking',
    'traffic',
    'aq',
    'csn',
    'smartpanel',
    'api',
    'authmultitoken',
    'smartcambridge'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # PostGIS
    'django.contrib.gis',

    # all auth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.google',

    # Django REST Framework
    'rest_framework',
    'corsheaders',
] + PROJECT_APPS

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'tfc_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'tfc_web.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'tfcweb',
    },
    'tfcserver': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'tfcserver',
    }
}

DATABASE_ROUTERS = ['tfc_web.dbrouter.CSNRouter']

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-gb'
TIME_FORMAT = 'H:i'
DATE_FORMAT = 'l j F Y'
TIME_ZONE = 'Europe/London'
USE_I18N = False
USE_L10N = False
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static_web/'
STATICFILES_DIRS = ["static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

API_ENDPOINT = 'http://localhost'
NEW_API_ENDPOINT = API_ENDPOINT
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATA_DIR = os.path.join(BASE_DIR, 'data')
TNDS_DIR = os.path.join(DATA_DIR, 'TNDS')
TNDS_NEW_DIR = os.path.join(DATA_DIR, 'TNDS_NEW')

# Web proxy
USE_X_FORWARDED_HOST = True

SITE_ID = 2

######## djang-allauth options ##########
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_PRESERVE_USERNAME_CASING = False
LOGIN_REDIRECT_URL = 'home'

######### Forum app (django-machina) configuration ##########
INSTALLED_APPS += [
    'mptt',
    'haystack',
    'widget_tweaks',
] + get_machina_apps()
MIDDLEWARE_CLASSES += [
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
]
TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'templates/forum'))
TEMPLATES[0]['DIRS'].append(MACHINA_MAIN_TEMPLATE_DIR)
TEMPLATES[0]['OPTIONS']['context_processors'].append('machina.core.context_processors.metadata')
STATICFILES_DIRS.append(MACHINA_MAIN_STATIC_DIR)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'machina_attachments': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp',
    }
}
HAYSTACK_CONNECTIONS = {
  'default': {
    'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
  },
}
MACHINA_FORUM_NAME = "SmartCambridge Forum"
MACHINA_DEFAULT_AUTHENTICATED_USER_FORUM_PERMISSIONS = [
    'can_see_forum',
    'can_read_forum',
    'can_start_new_topics',
    'can_reply_to_topics',
    'can_edit_own_posts',
    'can_post_without_approval',
    'can_create_polls',
    'can_vote_in_polls',
    'can_download_file',
]

###### everynet API #########
EVERYNET_API_ENDPOINT = "https://api.everynet.com/1.0.2/"

# TFC Server CSN API
TFC_SERVER_CSN_API = "http://localhost:8098/httpmsg/test/tfc.manager/msgrouter/test"

# Possible values as TNDS Zones
# East Anglia - EA
# East Midlands - EM
# London - L
# North East - NE
# North West - NW
# Scotland - S
# South East - SE
# South West - SW
# Cymru/Wales - W
# West Midlands - WM
# Yorkshire - Y
# National Coach Services Database - NCSD
TNDS_ZONES = ['EA', 'SE']

CORS_ORIGIN_ALLOW_ALL = True

# API configuration ====================================================

# Where to find the filesystem data
try:
    DATA_PATH = os.environ['TFC_API_DATA_PATH']
except KeyError:
    DATA_PATH = '/media/tfc'

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'token_burst': '1200/min',
        'token_sustained': '12000/hour',
    }
}

# ======================================================================

# An attempt to adapt the default Django logging to log useful stuff
# in development and production to the console (which will be captured
# and logged by Gunicorn)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detail': {
            'format': '[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s',
            'datefmt': '',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'detail',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    }
}
