from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SleepyConfig(AppConfig):
    name = 'sleepy'
    verbose_name = _('Sleepy')

    def ready(self):
        # We do like our application structure more than django's
        # so we import our modules manually.
        from sleepy.models import user  # noqa
