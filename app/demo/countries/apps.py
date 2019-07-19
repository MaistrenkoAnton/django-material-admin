from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CountriesConfig(AppConfig):
    name = 'demo.countries'
    icon_name = 'location_city'
    verbose_name = _('Countries')
