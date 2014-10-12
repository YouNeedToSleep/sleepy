from django.contrib import admin
from django.conf.urls import url, include, patterns

from sleepy.web import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='sleepy-index'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Hookup our REST Api
    url(r'^api/v1/', include('sleepy.api.v1.urls', namespace='api-v1')),

    url(r'^api/docs/', include('rest_framework.urls', namespace='rest_framework'))
)
