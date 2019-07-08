from django.db import models
from django.utils.translation import gettext_lazy as _


class DateModel(models.Model):
    date = models.DateField(_('Birth Date'))


class TimeModel(models.Model):
    time = models.TimeField(_('Time'))


class DateTimeModel(models.Model):
    time = models.DateTimeField(_('Date Time'))
