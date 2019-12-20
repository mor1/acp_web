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
from machina import MACHINA_MAIN_TEMPLATE_DIR, MACHINA_MAIN_STATIC_DIR
from tfc_web.secrets import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['smartcambridge.org', 'www.smartcambridge.org', '.cl.cam.ac.uk', 'localhost', '127.0.0.1', '[::1]']

ADMINS = [('SmartCambridge Admins', 'admin@smartcambridge.org')]
SERVER_EMAIL = 'root@smartcambridge.org'

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
    'smartcambridge',
    'bikes'
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

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
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
    }
}

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
    # Machina dependencies:
    'mptt',
    'haystack',
    'widget_tweaks',

    # Machina apps:
    'machina',
    'machina.apps.forum',
    'machina.apps.forum_conversation',
    'machina.apps.forum_conversation.forum_attachments',
    'machina.apps.forum_conversation.forum_polls',
    'machina.apps.forum_feeds',
    'machina.apps.forum_moderation',
    'machina.apps.forum_search',
    'machina.apps.forum_tracking',
    'machina.apps.forum_member',
    'machina.apps.forum_permission'
]
MIDDLEWARE += [
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
    'can_create_polls',
    'can_vote_in_polls',
    'can_download_file',
]

###### everynet API #########
EVERYNET_API_ENDPOINT = "https://ns.eu.everynet.io/api/v1.0/"

# CSN PREFIX. This is used to avoid conflicts between different application environments.
# We tag devices and filters in everynet using the user_id of the owner. To avoid conflicts
# between production and development environments we use this prefix to differentiate them.
CSN_PREFIX = 'dev'

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
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_THROTTLE_RATES': {
        'token_burst': '1200/min',
        'token_sustained': '12000/hour',
    }
}

# API authorisation settings ===========================================

TFC_PROD_USERNAME = 'tfc_prod'
TFC_PROD_EMAIL = 'cl-smartcambridge@lists.cam.ac.uk'
# TFC_PROD_PASSWORD = ''

# SYSTEM_API_TOKENS = { }
try:
    LOCAL_API_KEY = SYSTEM_API_TOKENS['TFC_WEB INTERNAL']['key']
    JS_API_KEY = SYSTEM_API_TOKENS['TFC_WEB JS']['key']
except NameError:
    LOCAL_API_KEY = ''
    JS_API_KEY = ''

# ======================================================================
# SMARTPANEL CONFIGURATION =============================================
# Everything prefixed by SMARTPANEL_ is passed to widget instances

SMARTPANEL_API_ENDPOINT = 'https://smartcambridge.org/api/v1/'
SMARTPANEL_API_TOKEN = JS_API_KEY

SMARTPANEL_TRAFFIC_MAP_RELOAD_LIMIT_DEFAULT = 10

# ======================================================================
# RTMONITOR_URI WEBSOCKET ENDPOINT =====================================

RTMONITOR_URI = 'https://smartcambridge.org/rtmonitor/sirivm/'

# ======================================================================
# 'Download API' configuration

DOWNLOAD_FEEDS = [
    {
        'name': 'aq',
        'title': 'Air Quality',
        'desc': 'Air Quality data from a selection of sensor stations deployed around '
                'Cambridge between June 2016 and February 2017.',
        'archive_by_default': True,
        'display': True,
        'first_year': 2016,
        'archives': [
            {
                'name': 'headers-year',
                'source_pattern': os.path.join('cam_aq/data_bin', '{date:%Y}', '*', '*', '*.json'),
                'destination': os.path.join('download_api', 'aq', 'aq-headers-{date:%Y}'),
                'extractor': 'api.extractors.aq.aq_header_extractor',
                'step': {'years': 1}

            },
            {
                'name': 'data-year',
                'source_pattern': os.path.join('cam_aq/data_bin', '{date:%Y}', '*', '*', '*.json'),
                'destination': os.path.join('download_api', 'aq', 'aq-data-{date:%Y}'),
                'extractor': 'api.extractors.aq.aq_data_extractor',
                'step': {'years': 1}
            },
            {
                'name': 'headers-month',
                'source_pattern': os.path.join('cam_aq/data_bin', '{date:%Y}', '{date:%m}', '*', '*.json'),
                'destination': os.path.join('download_api', 'aq', 'aq-headers-{date:%Y}-{date:%m}'),
                'extractor': 'api.extractors.aq.aq_header_extractor',
                'step': {'months': 1}
            },
            {
                'name': 'data-month',
                'source_pattern': os.path.join('cam_aq/data_bin', '{date:%Y}', '{date:%m}', '*', '*.json'),
                'destination': os.path.join('download_api', 'aq', 'aq-data-{date:%Y}-{date:%m}'),
                'extractor': 'api.extractors.aq.aq_data_extractor',
                'step': {'months': 1}
            },
        ],
        'metadata': {
            'source_pattern': os.path.join('sys', 'data_cam_aq_config', 'list.json'),
            'destination': os.path.join('download_api', 'aq', 'aq-metadata'),
            'extractor': 'api.extractors.aq.aq_metadata_extractor'
        }
    },
    {
        'name': 'parking',
        'title': 'Car Parking',
        'desc': 'Car Parking data showing the occupancy of Cambridge City Centre '
                'and Park and Ride car parks from 2017 onward.',
        'archive_by_default': True,
        'display': True,
        'first_year': 2017,
        'archives': [
            {
                'name': 'year',
                'source_pattern': os.path.join('cam_park_rss/data_park', '{date:%Y}', '*', '*', '*.txt'),
                'destination': os.path.join('download_api', 'parking', 'parking-{date:%Y}'),
                'extractor': 'api.extractors.parking.cam_park_rss_extractor',
                'step': {'years': 1}
            },
            {
                'name': 'month',
                'source_pattern': os.path.join('cam_park_rss/data_park', '{date:%Y}', '{date:%m}', '*', '*.txt'),
                'destination': os.path.join('download_api', 'parking', 'parking-{date:%Y}-{date:%m}'),
                'extractor': 'api.extractors.parking.cam_park_rss_extractor',
                'step': {'months': 1}
            },
            {
                'name': 'day',
                'source_pattern': os.path.join('cam_park_rss/data_park', '{date:%Y}', '{date:%m}', '{date:%d}', '*.txt'),
                'destination': os.path.join('download_api', 'parking', 'parking-{date:%Y}-{date:%m}-{date:%d}'),
                'extractor': 'api.extractors.parking.cam_park_rss_extractor',
                'start': {'day': 1},  # First of this month
                'step': {'days': 1}
            },

        ],
        'metadata': {
            'source_pattern': os.path.join('sys', 'data_parking_config', 'list.json'),
            'destination': os.path.join('download_api', 'parking', 'parking-metadata'),
            'extractor': 'api.extractors.parking.cam_park_rss_metadata_extractor'
        }
    },
    {
        'name': 'zone',
        'title': 'Traffic Speed',
        'desc': 'Traffic Speed data for a number of roads within Cambridge '
                'based on bus position reports from October 2017 onward.',
        'archive_by_default': True,
        'display': True,
        'first_year': 2017,
        'archives': [
            {
                'name': 'year',
                'source_pattern': os.path.join('cloudamber/sirivm/data_zone', '{date:%Y}', '*', '*', '*.txt'),
                'destination': os.path.join('download_api', 'zone', 'zone-{date:%Y}'),
                'extractor': 'api.extractors.zone.zone_extractor',
                'step': {'years': 1}
            },
            {
                'name': 'month',
                'source_pattern': os.path.join('cloudamber/sirivm/data_zone', '{date:%Y}', '{date:%m}', '*', '*.txt'),
                'destination': os.path.join('download_api', 'zone', 'zone-{date:%Y}-{date:%m}'),
                'extractor': 'api.extractors.zone.zone_extractor',
                'step': {'months': 1}
            },
            {
                'name': 'day',
                'source_pattern': os.path.join('cloudamber/sirivm/data_zone', '{date:%Y}', '{date:%m}', '{date:%d}', '*.txt'),
                'destination': os.path.join('download_api', 'zone', 'zone-{date:%Y}-{date:%m}-{date:%d}'),
                'extractor': 'api.extractors.zone.zone_extractor',
                'start': {'day': 1},  # First of this month
                'step': {'days': 1}
            },
        ],
        'metadata': {
            'source_pattern': os.path.join('sys', 'data_zone_config', 'list_all.json'),
            'destination': os.path.join('download_api', 'zone', 'zone-metadata'),
            'extractor': 'api.extractors.zone.zone_metadata_extractor'
        }
    },
    {
        'name': 'bus',
        'title': 'Bus position reports',
        'desc': 'Raw position reports from buses in the Cambridge area from October 2017 onward.',
        'archive_by_default': False,
        'display': False,
        'first_year': 2017,
        'archives': [
            {
                'name': 'month',
                'source_pattern': os.path.join('sirivm_json/data_bin/', '{date:%Y}', '{date:%m}', '*', '*.json'),
                'destination': os.path.join('download_private', 'bus', 'bus-{date:%Y}-{date:%m}'),
                'extractor': 'api.extractors.bus.bus_extractor',
                'step': {'months': 1}
            }
        ]
    }
]


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
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'smartcambridge.admin_email.AdminEmailHandler',
            'include_html': False,
        }
    },
    'loggers': {
        # Moved to settings_production
        #'django.request': {
        #    'handlers': ['mail_admins'],
        #    'level': 'ERROR',
        #    'propagate': False,
        #},
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    }

}
