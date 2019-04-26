from django.db import models
from django.utils.translation import gettext_lazy as _

from demo.countries.choices import COUNTRY_TYPES


class Country(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    picture = models.ImageField(_('Picture'), null=True, blank=True)
    population = models.IntegerField(null=True)
    type = models.CharField(_('Type'), choices=COUNTRY_TYPES, max_length=2)

    class Meta:
        verbose_name = _('County')
        verbose_name_plural = _('Countries')
        db_table = 'country'
        ordering = ('name',)



