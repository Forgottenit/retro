"""
Django settings for retro project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# colours 141529
# 98d2eb
# f433ab
# fbe689
# f39237
from pathlib import Path

import os
import dj_database_url

if os.path.isfile("env.py"):
    import env

    # CKEDITOR_CONFIGS = {
    #     "default": {
    #         "skin": "moono",
    #         # "skin": "office2013",
    #         "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
    #         "toolbar_YourCustomToolbarConfig": [
    #             {
    #                 "name": "document",
    #                 "items": [
    #                     "Source",
    #                     "-",
    #                     "Save",
    #                     "NewPage",
    #                     "Preview",
    #                     "Print",
    #                     "-",
    #                     "Templates",
    #                 ],
    #             },
    #             {
    #                 "name": "clipboard",
    #                 "items": [
    #                     "Cut",
    #                     "Copy",
    #                     "Paste",
    #                     "PasteText",
    #                     "PasteFromWord",
    #                     "-",
    #                     "Undo",
    #                     "Redo",
    #                 ],
    #             },
    #             {
    #                 "name": "editing",
    #                 "items": ["Find", "Replace", "-", "SelectAll"],
    #             },
    #             {
    #                 "name": "forms",
    #                 "items": [
    #                     "Form",
    #                     "Checkbox",
    #                     "Radio",
    #                     "TextField",
    #                     "Textarea",
    #                     "Select",
    #                     "Button",
    #                     "ImageButton",
    #                     "HiddenField",
    #                 ],
    #             },
    #             "/",
    #             {
    #                 "name": "basicstyles",
    #                 "items": [
    #                     "Bold",
    #                     "Italic",
    #                     "Underline",
    #                     "Strike",
    #                     "Subscript",
    #                     "Superscript",
    #                     "-",
    #                     "RemoveFormat",
    #                 ],
    #             },
    #             {
    #                 "name": "paragraph",
    #                 "items": [
    #                     "NumberedList",
    #                     "BulletedList",
    #                     "-",
    #                     "Outdent",
    #                     "Indent",
    #                     "-",
    #                     "Blockquote",
    #                     "CreateDiv",
    #                     "-",
    #                     "JustifyLeft",
    #                     "JustifyCenter",
    #                     "JustifyRight",
    #                     "JustifyBlock",
    #                     "-",
    #                     "BidiLtr",
    #                     "BidiRtl",
    #                     "Language",
    #                 ],
    #             },
    #             {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
    #             {
    #                 "name": "insert",
    #                 "items": [
    #                     "Image",
    #                     "Flash",
    #                     "Table",
    #                     "HorizontalRule",
    #                     "Smiley",
    #                     "SpecialChar",
    #                     "PageBreak",
    #                     "Iframe",
    #                 ],
    #             },
    #             "/",
    #             {
    #                 "name": "styles",
    #                 "items": ["Styles", "Format", "Font", "FontSize"],
    #             },
    #             {"name": "colors", "items": ["TextColor", "BGColor"]},
    #             {"name": "tools", "items": ["Maximize", "ShowBlocks"]},
    #             {"name": "about", "items": ["About"]},
    #             "/",  # put this to force next toolbar on new line
    #             {
    #                 "name": "yourcustomtools",
    #                 "items": [
    #                     # put the name of your editor.ui.addButton here
    #                     "Preview",
    #                     "Maximize",
    #                 ],
    #             },
    #         ],
    #         "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
    #         "toolbarGroups": [
    #             {
    #                 "name": "document",
    #                 "groups": ["mode", "document", "doctools"],
    #             }
    #         ],
    #         "height": 291,
    #         "width": "100%",
    #         "filebrowserWindowHeight": 725,
    #         "filebrowserWindowWidth": 940,
    #         "toolbarCanCollapse": True,
    #         "mathJaxLib": "//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML",
    #         "tabSpaces": 4,
    #         "extraPlugins": ",".join(
    #             [
    #                 "uploadimage",  # the upload image feature
    #                 # your extra plugins here
    #                 "div",
    #                 "autolink",
    #                 "autoembed",
    #                 "embedsemantic",
    #                 "autogrow",
    #                 # 'devtools',
    #                 "widget",
    #                 "lineutils",
    #                 "clipboard",
    #                 "dialog",
    #                 "dialogui",
    #                 "elementspath",
    #             ]
    #         ),
    #     }
    # }

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")

DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000

# Spotify Secret Key

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET", "")

# Spotify Access Token and expiration, set in product_data app - spotify_api
SPOTIFY_ACCESS_TOKEN = None
SPOTIFY_TOKEN_EXPIRY_TIME = None

# STRIPE SECRET KEYS and settings
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY", "")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_WH_SECRET = os.environ.get("STRIPE_WH_SECRET")
DEFAULT_FROM_EMAIL = "forgottenit@example.com"

STRIPE_CURRENCY = "eur"
FREE_DELIVERY_THRESHOLD = 40
STANDARD_DELIVERY_PERCENTAGE = 10


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get("DEVELOPMENT")

# STAR_RATINGS_ANONYMOUS = True
ALLOWED_HOSTS = [
    "forgottenit-retro.herokuapp.com",
    "https://forgottenit-retro.herokuapp.com/*",
    "localhost",
    ".gitpod.io",
    "https://8000-forgottenit-retro-s9wz1pwll0t.ws-eu101.gitpod.io",
    "https://8000-forgottenit-retro-vhpue5nw9jo.ws-eu101.gitpod.io/",
]

# Required CSRF_TRUSTED_ORIGINS for Django 4.2
CSRF_TRUSTED_ORIGINS = [
    "https://forgottenit-retro.herokuapp.com",
    "https://localhost",
    "https://8000-forgottenit-retro-s9wz1pwll0t.ws-eu101.gitpod.io",
    "https://8000-forgottenit-retro-vhpue5nw9jo.ws-eu101.gitpod.io",
    "https://.gitpod.io",
    "https://dashboard.stripe.com",
    "https://js.stripe.com/",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",
    "django.contrib.staticfiles",
    "cloudinary",
    "django.contrib.sites",
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
    "home",
    "fixtures",
    "accounts",
    "products",
    "product_data",
    "django_user_agents",
    "cart",
    "checkout",
    "django_extensions",
    "ckeditor",
    "star_ratings",
]

SOCIALACCOUNT_PROVIDERS = {
    "facebook": {
        "APP": {
            "client_id": "your-facebook-app-client-id",
            "secret": "your-facebook-app-secret",
        }
    },
    "google": {
        "APP": {
            "client_id": "your-google-app-client-id",
            "secret": "your-google-app-secret",
        }
    },
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "retro.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # required by allauth
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "cart.contexts.cart_contents",
            ],
            "builtins": [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
        },
    },
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = "/accounts/login"
LOGIN_REDIRECT_URL = "/"

WSGI_APPLICATION = "retro.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if os.environ.get("DEVELOPMENT") == "1" or os.environ.get("DEBUG") == "1":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Dublin"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
STATICFILES_STORAGE = (
    "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
)
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

if "DEVELOPMENT" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    DEFAULT_FROM_EMAIL = "forgottenitretro@gmail.com"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASS")
    DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
