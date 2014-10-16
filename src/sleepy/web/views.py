from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView, TemplateView
from django.utils.http import is_safe_url
from django.utils.translation import ugettext


class IndexView(TemplateView):
    """View for the index page"""
    template_name = 'sleepy/web/index.html'


class LogoutView(RedirectView):
    url = reverse_lazy('home')
    permanent = False

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(self.request)
            messages.success(request, ugettext('You have successfully logged out.'))

        return super(LogoutView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        url = super(LogoutView, self).get_redirect_url(*args, **kwargs)
        next_url = self.request.REQUEST.get(REDIRECT_FIELD_NAME, None)

        if next_url and is_safe_url(url=next_url, host=self.request.get_host()):
            url = next_url

        return url
