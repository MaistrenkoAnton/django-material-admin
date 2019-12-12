from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from demo.countries.choices import COUNTRY_TYPES


class Country(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    picture = models.ImageField(_('Picture'), null=True, blank=True)
    population = models.IntegerField(_('Population'), null=True)
    type = models.CharField(_('Type'), choices=COUNTRY_TYPES, max_length=2)
    is_safe = models.BooleanField(_('Is safe'), default=True)
    created = models.DateField(_('Created'))
    modified = models.DateTimeField(_('Modified'))
    time = models.TimeField(_('Time'))

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        db_table = 'country'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Person(models.Model):
    uuid = models.UUIDField(_('UUID number'))
    nationality = models.ForeignKey(
        'countries.Country', verbose_name=_('Nationality'), on_delete=models.CASCADE, null=True, blank=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('User'), on_delete=models.CASCADE, null=True, blank=True
    )
    date = models.DateField(_('Birth Date'))
    description = models.TextField(_('description'), null=True, blank=True)
    google_play = models.URLField(_('Google Play Link'), blank=True, null=True)
    spotify = models.URLField(_('Spotify Link'), blank=True, null=True)
    itunes = models.URLField(_('Itunes Link'), blank=True, null=True)
    video = models.FileField(_('Video'), null=True, blank=True)
    smart = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
        db_table = 'persons'


class ProxyPerson(Person):
    class Meta:
        proxy = True
        verbose_name = _('Proxy Person')
        verbose_name_plural = _('Proxy Persons')
