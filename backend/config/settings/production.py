from .base import *

DEBUG = False

ALLOWED_HOSTS = ['djargova-backend.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

# Activate Django-Heroku.
django_heroku.settings(locals())
