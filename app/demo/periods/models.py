from django.db import models
from django.utils.translation import gettext_lazy as _


class DateModel(models.Model):
    date = models.DateField(_('Birth Date'))

    class Meta:
        verbose_name = _('Date Model')
        verbose_name_plural = _('Date Models')


class TimeModel(models.Model):
    time = models.TimeField(_('Time'))

    class Meta:
        verbose_name = _('Time Model')
        verbose_name_plural = _('Time Models')


class DateTimeModel(models.Model):
    time = models.DateTimeField(_('Date Time'))

    class Meta:
        verbose_name = _('Date Time Model')
        verbose_name_plural = _('Date Time Models')
