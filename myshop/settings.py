"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os.path
from pathlib import Path
import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-3xbex1p$x_ty&ujaz!*k%s*tza82kj6=6#g^=^06kf)a8!z0xb'

# SECURITY WARNING: don't run with debug turned on in production!
env = environ.Env(
    DEBUG=(bool, False),
)
environ.Env.read_env()

DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

# Конфигурация сервера электронной почты
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
#следует ли использовать защищенное соединение транспортного слоя
EMAIL_USE_TLS = True
# следует ли использовать неявное защищенное соединение TLS.
EMAIL_USE_SSL = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CART_SESSION_ID = 'cart'

# Настроечные параметры Stripe
STRIPE_PUBLISHABLE_KEY = 'pk_test_51PIptXCcCcq46GGFtH07fVLuVzzIbaiuNfATDS15A9NvzCDKZZhVhtPC9Vyn7WT91cyCEERwLyDklZ1EqvVXe3qp00yuHVSA0I' # Публикуемый ключ
STRIPE_SECRET_KEY = 'sk_test_51PIptXCcCcq46GGFYoKEzjplUR7C2veL76Fw7buxYJnbGHEwSgE7FmLDEqu1QdYRK3IFPddC5Vm8xIU5i3J1iuLm00xy6LPG4e' # Секретный ключ
STRIPE_API_VERSION = '2022-08-01'


# Application definition
LOGOUT_REDIRECT_URL = "/home"
LOGIN_REDIRECT_URL = '/home'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'accounts',
    'cart',
    'orders',
    'payment',
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

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myshopdb',
        'USER': 'shopadmin',
        'PASSWORD': 'djangopasswd',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}"""

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
