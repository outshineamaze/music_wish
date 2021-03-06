"""
Django settings for bestwish project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
#coding:utf-8
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
import os.path 

from os import environ
#debug = not environ.get("myoutshine", "") 
DEBUG = False



if DEBUG :
    MYSQL_DB = 'music_wish'
    MYSQL_USER = 'root' 
    MYSQL_PASS = '' 
    MYSQL_HOST_M = 'localhost' 
    MYSQL_HOST_S = 'localhost' 
    MYSQL_PORT = '3306' 
else :
    MYSQL_DB = 'music_wish'
    MYSQL_USER = 'root' 
    MYSQL_PASS = '**********' 
    MYSQL_HOST_M = 'localhost' 
    MYSQL_HOST_S = 'localhost' 
    MYSQL_PORT = '3306' 


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r3eb7!#-#kdbk(%*r7e769p7-(1tbpdpi6h1qr%%%v+@3usj^8'

# SECURITY WARNING: don't run with debug turned on in production!


TEMPLATE_DEBUG = False

ALLOWED_HOSTS = True


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'comments'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bestwish.urls'

WSGI_APPLICATION = 'bestwish.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': MYSQL_DB, 
        'USER': MYSQL_USER, 
        'PASSWORD': MYSQL_PASS, 
        'HOST': MYSQL_HOST_M, 
        'PORT': MYSQL_PORT, 
}
}

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = (
          os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'),
    )
