from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _, ugettext

from social import exceptions as exc
from social.apps.django_app import middleware


MESSAGES = {
    exc.AuthStateMissing: _('Authentication could not be validated.'),
    exc.AuthStateForbidden: _('Authentication could not be validated.'),
    exc.AuthAlreadyAssociated: _(
        'A different user already registered with this credentials.'),
    exc.AuthTokenRevoked: _('You revoked access for this account.'),
    exc.AuthForbidden: _('Your credentials are not allowed.'),
    exc.InvalidEmail: _('The Email could not be validated.')
}


class SocialAuthExceptionMiddleware(middleware.SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        self.strategy = getattr(request, 'social_strategy', None)
        if self.strategy is None or self.raise_exception(request, exception):
            return

        if isinstance(exception, exc.SocialAuthBaseException):
            message = self.get_message(request, exception)
            url = self.get_redirect_uri(request, exception)
            messages.error(request, message, self.strategy.backend.name)
            return redirect(url)

    def get_message(self, request, exception):
        if type(exception) in MESSAGES:
            return MESSAGES[type(exception)]
        elif isinstance(exception, exc.AuthFailed):
            if exception.message == 'access_denied':
                return ugettext('Authentication process was canceled.')
            return ugettext('Authentication failed.')
        elif isinstance(exception, exc.AuthCanceled):
            return ugettext('Authentication process was canceled.')
        else:
            # Exceptions might have a message, but maybe not!
            return exception.message or ugettext(
                'An unknown error happened while authenticating.')
