from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        null=True,
        blank=True
    )
    picture = models.FileField(
        _('User Picture'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Picture')
        verbose_name_plural = _('Picture')
        db_table = 'user_pictures'
