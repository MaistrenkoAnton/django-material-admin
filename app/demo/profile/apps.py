from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProfileConfig(AppConfig):
    name = 'demo.profile'
    icon_name = 'layers'
    verbose_name = _('Profile')
