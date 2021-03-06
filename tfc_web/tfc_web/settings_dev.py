from tfc_web.settings import *

# Allow configuration of test-suite database from environment variables. A
# variable DJANGO_DB_<key> will override the DATABASES['default'][<key>]
# setting.
_db_envvar_prefix = 'DJANGO_DB_'
for name, value in os.environ.items():
    # Only look at variables which start with the prefix we expect
    if not name.startswith(_db_envvar_prefix):
        continue

    # Remove prefix
    name = name[len(_db_envvar_prefix):]

    # Set value
    DATABASES['default'][name] = value

# Set the API data path to point to the internal test data
DATA_PATH = '/usr/src/app/api/tests/data'

NEW_API_ENDPOINT = 'http://127.0.0.1:8000'

SMARTPANEL_API_ENDPOINT = 'https://smartcambridge.org/api/v1/'

ALLOWED_HOSTS = ['*']

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
        'level': 'DEBUG',
    }
}

EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST', 'localhost')
EMAIL_PORT = int(os.environ.get('DJANGO_EMAIL_PORT', '25'))
