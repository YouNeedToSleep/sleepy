from django.contrib import admin
from django.conf.urls import url, include, patterns

from sleepy.web import views


urlpatterns = patterns('',
    # Regular views
    url(r'^$', views.IndexView.as_view(),
        name='sleepy-home'),

    url(r'^accounts/logout/$', views.LogoutView.as_view(),
        name='sleepy-logout'),

    url(r'^accounts/', include('social.apps.django_app.urls', namespace='social')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Hookup our REST Api
    url(r'^api/v1/', include('sleepy.api.v1.urls', namespace='v1')),

    url(r'^api/docs/', include('rest_framework.urls', namespace='rest_framework'))
)
