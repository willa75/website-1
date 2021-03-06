from ._base import *  # noqa

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

DEBUG = True

SECRET_KEY = 'PYSLACKERS_DEVELOPMENT_SECRET_KEY'
