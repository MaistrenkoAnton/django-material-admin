from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RelationsConfig(AppConfig):
    name = 'demo.relations'
    icon_name = 'layers'
    verbose_name = _('Relations')
