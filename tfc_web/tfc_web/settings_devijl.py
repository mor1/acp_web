# ijl20 dev settings
# as production except DEBUG=true and no https redirect

from tfc_web.settings import *

DEBUG = True

DEFAULT_FROM_EMAIL = "smart-cambridge@cl.cam.ac.uk"
EMAIL_HOST = "ppsw.cam.ac.uk"
EMAIL_PORT = 25

TFC_SERVER_CSN_API = "http://localhost/httpmsg/A/tfc.manager/msgrouter/A"
