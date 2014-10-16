from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from social.backends.email import EmailAuth as PsaEmailAuth
from social.exceptions import AuthException, AuthMissingParameter


class EmailAuth(PsaEmailAuth):
    def get_user_id(self, details, response):
        user_id = super(EmailAuth, self).get_user_id(details, response)

        if user_id and not self.setting('USER_ID_CASE_SENSITIVE', False):
            # Emails shouldn't be case sensitive, lets check if we have a
            # user_id. If yes, try to finde the correct-cased value.

            user_model = self.strategy.storage.user.user_model()

            try:
                user_id = getattr(user_model.objects.get(
                    **{'{0}__iexact'.format(self.ID_KEY): user_id}
                ), self.ID_KEY)
            except user_model.DoesNotExist:
                pass

        if user_id:
            try:
                validate_email(user_id)
            except ValidationError as ex:
                raise AuthException(self.strategy.backend, ex.message)

        return user_id

    def auth_complete(self, *args, **kwargs):
        # The signup view for email login stores its data in a session, we use
        # this data if the request data is empty or not set.
        data = self.data or self.strategy.session_get('signup_data', {})

        # Its essential that an email address is provided, because we use this
        # field for looking up the user and user social auth objects.
        if self.ID_KEY not in data:
            raise AuthMissingParameter(self, self.ID_KEY)

        kwargs.update({'response': data, 'backend': self})
        return self.strategy.authenticate(*args, **kwargs)
