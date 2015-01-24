from base import *


########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
########## END CACHE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
########## END TEMPLATE CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
########## END EMAIL CONFIGURATION


########## LOGGING CONFIGURATION
# Break tests when a datetime receives a naive datetime
import warnings

warnings.filterwarnings(
    'error', r"DateTimeField received a naive datetime",
    RuntimeWarning, r'django\.db\.models\.fields')
########## END LOGGING CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"tL&JYCEY57c]g^Vh^cMqg2(/g2*+^ou5=QBM7[9C&x3\G;1uS+"
########## END SECRET CONFIGURATION


########## MEDIA CONFIGURATION
MEDIA_ROOT = project_path('media')
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
STATIC_ROOT = project_path('static')
########## END STATIC FILE CONFIGURATION


########## COMPRESSOR CONFIGURATION
COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = []
########## END CONFIGURATION