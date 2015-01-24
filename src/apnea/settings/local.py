from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': project_path('src', 'apnea', 'db.sqlite3'),
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

COMPRESS_ENABLED = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

INTERNAL_IPS = ('127.0.0.1')

SECRET_KEY = "|-88pPZr)McRp]x^2zECo0f32jH:z$MQBUD!A+EWS>d66]fyp4"

ALLOWED_HOSTS = [u'localhost', u'localhost:8000', u'apnea.dev']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = project_path('media')

STATIC_ROOT = project_path('static')