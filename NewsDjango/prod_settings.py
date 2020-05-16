import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'kaifu=-we1234gfs$$@$@$&#ja4n*%ko$zn'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_news',
        'USER': 'dj_admin',
        'PASSWORD': 'qwerty123',
        'HOST': 'localhost',
        'PORT': '5432',
        
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')