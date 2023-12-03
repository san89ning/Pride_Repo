"""
Django settings for pridehouzz project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static\script', 'serviceworker.js')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ilgn(ir3z)vpa**glap6m)))h!xniq5%g@(!gi%+u0^_7)=&j)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CART_SESSION_ID = 'cart'
SESSION_COOKIE_AGE = 86400

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'pwa',
    'core',
    'store',
    'userprofile'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pridehouzz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'pridehouzz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Progressive web App

PWA_CONFIG = {
    "name": "pridehouzz",
    "short_name": "P26",
    "theme_color": "#000",
    "background_color": "#000",
    "display": "standalone",
    "orientation": "any",
    "scope": "/",
    "start_url": "/",
    "icons": [
        {
           "src": "/static/images/logo/brand-logo1.png",
           "type": "image/png",
           "sizes": "72x72"
        },
        {
                        "src": "/static/images/logo/brand-logo1.png",
                        "type": "image/png",
                        "sizes": "96x96"
                },
                {
                        "src": "/static/images/logo/brand-logo1.png",
                        "type": "image/png",
                        "sizes": "128x128"
                },
                {
                        "src": "/static/images/logo/brand-logo1.png",
                        "type": "image/png",
                        "sizes": "144x144"
                },
                {
                        "src": "/static/images/logo/brand-logo1.png",
                        "type": "image/png",
                        "sizes": "152x152"
                },
                {
                        "src": "/static/images/logo/brand-logo1.png",
                        "type": "image/png",
                        "sizes": "192x192"
                },
                {
                        "src": "/static/images/logo/brand-logo1.png",
                        "type": "image/png",
                        "sizes": "384x384"
                },
                {
                        "src": "/static/images/logo/brand-logo1.png",
                        "type": "image/png",
                        "sizes": "512x512"
                }
    ],
     "lang": "en",
        "dir": "ltr",
        "description": "Progressive Web app powerd by Django",
        "version": "1.",
        "manifest_version": "1.0",
        "permissions": [
                "notifications",
                "webRequest"
        ],
        "author": "PWA-django"
}