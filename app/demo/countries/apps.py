from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CountriesConfig(AppConfig):
    name = 'demo.countries'
    icon_name = 'location_city'
    verbose_name = _('Countries')
