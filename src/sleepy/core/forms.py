from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = settings.SOCIAL_AUTH_USER_DETAILS_FIELDS

    def clean_email(self):
        email = self.cleaned_data.get('email', None)

        if email and self._meta.model.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(_('This email address is already in use.'))

        return email


class UserSignupForm(UserDetailsForm):
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password_repeat = forms.CharField(label=_('Password repeat'), widget=forms.PasswordInput)

    def clean(self):
        password = self.cleaned_data.get('password', None)
        password_repeat = self.cleaned_data.get('password_repeat', None)

        if password and password_repeat:
            if password != password_repeat:
                raise forms.ValidationError(_('Password missmatch.'))

        return self.cleaned_data
