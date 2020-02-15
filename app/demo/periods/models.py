from django.db import models
from django.utils.translation import gettext_lazy as _


class DateModel(models.Model):
    date = models.DateField(_('Birth Date'))
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('my_order',)
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


class Period1(models.Model):
    period = models.CharField(_('Period1'), max_length=255)

    class Meta:
        verbose_name = _('Period1')
        verbose_name_plural = _('Periods1')


class Period2(models.Model):
    period = models.CharField(_('Period2'), max_length=255)

    class Meta:
        verbose_name = _('Period2')
        verbose_name_plural = _('Periods2')


class Period3(models.Model):
    period = models.CharField(_('Period3'), max_length=255)

    class Meta:
        verbose_name = _('Period3')
        verbose_name_plural = _('Periods3')


class Period4(models.Model):
    period = models.CharField(_('Period4'), max_length=255)

    class Meta:
        verbose_name = _('Period4')
        verbose_name_plural = _('Periods4')


class Period5(models.Model):
    period = models.CharField(_('Period5'), max_length=255)

    class Meta:
        verbose_name = _('Period5')
        verbose_name_plural = _('Periods5')