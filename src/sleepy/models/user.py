# -*- coding: utf-8 -*-
"""
    sleepy.models.user
    ~~~~~~~~~~~~~~~~~~

    User model.
"""
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, UserManager
from uuidfield import UUIDField


class User(AbstractBaseUser):
    username = models.TextField(_('Username'),
        max_length=50, null=True, unique=True)
    email = models.EmailField(_('Email'), max_length=254, unique=True)
    name = models.TextField(_('Name'), max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    is_superuser = models.BooleanField(
        _('superuser status'), default=False,
        help_text=_('Designates that this user has all permissions without '
                    'explicitly assigning them.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    api_key = UUIDField(auto=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return self.is_superuser
