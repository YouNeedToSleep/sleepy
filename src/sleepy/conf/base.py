import os
from django.core.urlresolvers import reverse_lazy
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, '..', '..')

SECRET_KEY = 'na2p&yexkp-g83$2m^&b!r+a%nv2ci1!d9vh^a_7h!hv*7&h79'

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # i18n/l10n
    'django_babel',
    'statici18n',

    # For our REST Api
    'rest_framework',

    # Social Authentication
    'social.apps.django_app.default',

    # Sleepy apps
    'sleepy',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sleepy.urls'

WSGI_APPLICATION = 'sleepy.wsgi.application'

AUTH_USER_MODEL = 'sleepy.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'bower_components'),
    os.path.join(PROJECT_DIR, 'src', 'sleepy', 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'src', 'sleepy', 'templates'),
)

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'src/sleepy/locale'),
    os.path.join(PROJECT_DIR, 'src/sleepy/templates/locale'),
)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'web', 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'web', 'media')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'formatters': {
        'verbose': {
            'format':
                '[%(asctime)s] %(levelname)s:%(name)s %(funcName)s\n %(message)s',  # noqa
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        # This is the root logger that catches everything, if there's no other
        # match on the logger name. If we want custom logging handing for our
        # code vs. third-party code, define loggers for each module/app
        # that's using standard python logging.
        'root': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'celery': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'sleepy': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Django security related settings.
SECURE_SSL_REDIRECT = True

# Force cookies to be https only (or at least tell the browsers to do so...)
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

# Django REST Framework related settings.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'sleepy.core.social_backends.EmailAuth',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = reverse_lazy('social:begin', args=('email',))
LOGIN_REDIRECT_URL = reverse_lazy('sleepy-home')
LOGIN_ERROR_URL = LOGIN_URL

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_login.html'

SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_USER_DETAILS_FIELDS = ('email',)

# We need to add username if we have a user model with username, even if we
# don't use the username.
SOCIAL_AUTH_USER_FIELDS = ('username',) + SOCIAL_AUTH_USER_DETAILS_FIELDS

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
)
