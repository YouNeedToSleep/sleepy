import os.path
import os

import pytest
from django.conf import settings
from pytest_django.lazy_django import skip_if_no_django


def pytest_configure(config):
    if not settings.configured:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'sleepy.conf.test'

    # override a few things with our test specifics
    settings.INSTALLED_APPS = tuple(settings.INSTALLED_APPS) + (
        'sleepy.tests',
    )
