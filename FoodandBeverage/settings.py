import os
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = "3c5!dl+@)a9o0q(i3q%4e_ab%w#*unc@ut-y-%k+lm3j"


DEBUG = True

ALLOWED_HOSTS = ["foodandbeveragenepal.herokuapp.com"]
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"

INSTALLED_APPS = [
    "jazzmin",
    "users.apps.UsersConfig",
    "contact.apps.ContactConfig",
    "team.apps.TeamConfig",
    "blog.apps.BlogConfig",
    "posts.apps.PostsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "embed_video",
    "django.contrib.humanize",
    "payments.apps.PaymentsConfig",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "FoodandBeverage.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],  # this is very important
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "FoodandBeverage.wsgi.application"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'foodandbeverage',
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "fooddb",
#         "USER": "postgres",
#         "PASSWORD": "karki582465",
#         "HOST": "localhost",
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "FoodandBeverage/static")]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIl")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")

LOGIN_URL = "login"

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get("EMAIl")
# EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")


STRIPE_SECRET_KEY = "pk_test_ibLPwjOu7aM4TKeqqfN4eueS3iF2236l"
STRIPE_PUBLISHABLE_KEY = "sk_test_3RTuvScWNJm0dVwjvW3LwK050hW0JEJ"

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {messages.ERROR: "danger"}


django_heroku.settings(locals())
