from tfc_web.settings import *
from tfc_web.secrets import DATABASE_PASSWORD

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'tfcweb',
        'USER': 'tfcwebuser',
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}

API_ENDPOINT = 'http://smartcambridge.org'
