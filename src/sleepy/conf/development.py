from sleepy.conf.base import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sleepy_dev',
    }
}


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''  # noqa
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''

LOGGING['loggers']['root']['level'] = 'DEBUG'
LOGGING['loggers']['celery']['level'] = 'DEBUG'
LOGGING['loggers']['sleepy']['level'] = 'DEBUG'


SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
