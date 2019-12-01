# -*- coding: utf-8 -*-
import os


ALLOWED_HOSTS = ['*']
DEBUG = True
SECRET_KEY = 'psst'
SITE_ID = 1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_URLCONF = 'mock_master.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    # 'south',
    'django_nose',
    'mock_master',
    'djangomaster',
)


STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.static",
)

LOGIN_URL = '/admin/'

TEST_RUNNER = 'djangomaster.tests.MasterNoseTestSuiteRunner'

NOSE_ARGS = ['--with-cov', '--cov-report', 'html', '--nologcapture']
