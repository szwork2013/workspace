"""
Django settings for article project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import abspath,dirname,basename
#プロジェクトのルートをSITE_ROOTとする
SITE_ROOT=abspath(os.path.join(dirname(__file__),".."))
#静的ファイルを保存するフォルダ名を設定
STATIC_URL='/static/'
#静的ファイルを保存するフォルダのパスを設定
STATICFILES_DIRS=(os.path.join(SITE_ROOT,'static'),)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_PATH=os.path.abspath(os.path.split(__file__)[0])
MEDIA_ROOT=os.path.join(BASE_PATH,'static')
MEDIA_URL='/static_site/'

TEMPLATE_DIRS=(
		os.path.join(BASE_DIR,'templates')
		)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vd)749_a4pn)f$alflen=ob%=kj6tq!ppmg5fm(7-lsr_5aa#$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'pub',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'article.urls'

WSGI_APPLICATION = 'article.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
