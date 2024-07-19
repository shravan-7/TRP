"""
Django settings for Tourist_Place_recommendation project.

Generated by 'django-admin startproject' using Django 3.2.25.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
import dj_database_url

from dotenv import load_dotenv

load_dotenv()
import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.debug("Starting application...")
logger.debug(f"Database URL: {os.getenv('DATABASE_URL')}")
logger.debug(f"SSL cert file exists: {os.path.exists('/app/ca.pem')}")


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
AUTH_USER_MODEL = "Tourist_App.User"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-n=uge+d#zm1jf!&hl@0+opg(%vbmdlrm=o8xz^hmjf6m13kre6"
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-n=uge+d#zm1jf!&hl@0+opg(%vbmdlrm=o8xz^hmjf6m13kre6')
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False").lower() == "True"

# ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost", ".vercel.app", ".show.sh",".tpr-azure.vercel.app"]
ALLOWED_HOSTS = ['tpr-production.up.railway.app', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Tourist_App",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
WHITENOISE_MANIFEST_STRICT = False
CSRF_TRUSTED_ORIGINS = ['https://tpr-production.up.railway.app']
# CSRF_TRUSTED_ORIGINS = ["https://tpr-production.up.railway.app"]
ROOT_URLCONF = "Tourist_Place_Recommendation.urls"

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# After each major configuration section


# etc.

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#     },
#     "root": {
#         "handlers": ["console"],
#         "level": "INFO",  # Change this to INFO
#     },
# }

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Tourist_Place_Recommendation.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'tourist_place_db',
#         'USER' : 'root',
#         'PASSWORD': '12345678',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.getenv('DB_NAME', 'tourist_place_db'),
#         'USER': os.getenv('DB_USER', 'root'),
#         'PASSWORD': os.getenv('DB_PASSWORD', 'root'),
#         'HOST': os.getenv('DB_HOST', 'localhost'),
#         'PORT': os.getenv('DB_PORT', '33333')
#     }
# }
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
# DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)
# DATABASES["default"]["OPTIONS"]["charset"] = "utf8mb4"
# del DATABASES["default"]["OPTIONS"]["sslmode"]
# DATABASES["default"]["OPTIONS"]["ssl"] = {"ca": os.environ.get("MYSQL_ATTR_SSL_CA")}

# DATABASES = {
#     "default": dj_database_url.config(
#         default=os.getenv("DATABASE_URL"),
#         conn_max_age=600,
#         ssl_require=True
#     )
# }
# # Set the charset option
# DATABASES["default"]["OPTIONS"]["charset"] = "utf8mb4"

# # Remove the sslmode option if it exists
# if "sslmode" in DATABASES["default"]["OPTIONS"]:
#     del DATABASES["default"]["OPTIONS"]["sslmode"]

# # Add SSL options for MySQL using the MYSQL_ATTR_SSL_CA environment variable
# DATABASES["default"]["OPTIONS"]["ssl"] = {"ca": os.getenv("MYSQL_ATTR_SSL_CA")}

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# Update SSL options
if os.path.exists("/app/ca.pem"):
    DATABASES["default"]["OPTIONS"] = {
        "ssl": {"ca": "/app/ca.pem"}
    }
logger.debug("Database configuration complete")
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

API_KEY = "us3Mhv7Bl4U4W2G3UnRMbwZnZlRcFJ2mbhS4emfDzxg"

API_KEY_OTP = "3154af6c-900c-11ee-8cbb-0200cd936042"

APPEND_SLASH = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = "static/"
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# # STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), os.path.join(BASE_DIR, "file")]
# # STATICFILES_DIRS = [BASE_DIR / "static"]
# STATICFILES_DIRS = [BASE_DIR / "Tourist_App" / "static"]
# # STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build" "static")
# STATIC_ROOT = BASE_DIR / "staticfiles_build"
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'Tourist_App', 'static'),
# ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
# # STATIC_ROOT = BASE_DIR / 'staticfiles_build' / 'static'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Tourist_App', 'static'),
]
logger.debug("Static files configuration complete")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from django.contrib.messages import constants as messages


MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}
