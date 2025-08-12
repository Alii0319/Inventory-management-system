import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(vpnokgy(6$*3+65jhu=9oq9wte!vyd+$0$olfp6x93ye%tkd&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Environment variables se ALLOWED_HOSTS set karo
ALLOWED_HOSTS = [
   "inventory-management-system-production-10fa.up.railway.app",
   "127.0.0.1",
   "localhost"
]

# Railway environment variable check
railway_host = os.environ.get('ALLOWED_HOSTS')
if railway_host:
   ALLOWED_HOSTS.extend(railway_host.split(','))

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
   'https://inventory-management-system-production-10fa.up.railway.app',
   'http://inventory-management-system-production-10fa.up.railway.app',
]

# Railway environment variable check for CSRF
csrf_origins = os.environ.get('CSRF_TRUSTED_ORIGINS')
if csrf_origins:
   CSRF_TRUSTED_ORIGINS.extend(csrf_origins.split(','))

# Additional CSRF settings for Railway
CSRF_COOKIE_SECURE = False
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'Lax'

# Session settings
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = 'Lax'

# Application definition
INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'inventory',
   'rest_framework',
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

ROOT_URLCONF = 'inventory_system.urls'

TEMPLATES = [
   {
       'BACKEND': 'django.template.backends.django.DjangoTemplates',
       'DIRS': [BASE_DIR / 'templates'],
       'APP_DIRS': True,
       'OPTIONS': {
           'context_processors': [
               'django.template.context_processors.request',
               'django.contrib.auth.context_processors.auth',
               'django.contrib.messages.context_processors.messages',
           ],
       },
   },
]

WSGI_APPLICATION = 'inventory_system.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',
   }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': [
       'rest_framework.authentication.SessionAuthentication',
   ],
   'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.IsAuthenticatedOrReadOnly',
   ],
}