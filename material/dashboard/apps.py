from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DashboardMaterialConfig(AppConfig):
    name = 'material.dashboard'
    icon_name = 'dashboard'
    verbose_name = _('Dashboard')
