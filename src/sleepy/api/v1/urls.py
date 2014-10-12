from django.conf.urls import url, patterns

from sleepy.api.v1 import users


urlpatterns = patterns('',
    # Hookup our REST Api
    url(r'^users/', users.ListView.as_view())
)
