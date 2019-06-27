from django.contrib.admin.sites import AdminSite
from django.utils.functional import LazyObject
from django.utils.html import strip_tags
from django.utils.module_loading import import_string
from django.apps import apps


class MaterialAdminSite(AdminSite):
    """Extends AdminSite to add material design for admin interface"""
    default_config_mapping = {
        'auth': 'group',
        'sites': 'web'
    }

    def __init__(self, name='material'):
        super().__init__(name)
        self.login_template = 'material/login.html'
        self.logout_template = 'material/logout.html'
        self.index_template = 'material/index.html'
        self.password_change_template = 'material/password_change.html'

    def _build_app_dict(self, request, label=None):
        """
        Build the app dictionary. The optional `label` parameter filters models
        of a specific app. Adding material icons, default icons.
        """
        app_dict = super()._build_app_dict(request, label)
        for key in app_dict:
            icon = getattr(apps.get_app_config(key), 'icon_name', None) or self.default_config_mapping.get(key)
            if icon:
                app_dict[key]['icon'] = strip_tags(icon)
        return app_dict


class DefaultMaterialAdminSite(LazyObject):
    def _setup(self):
        AdminSiteClass = import_string(apps.get_app_config('material').default_site)
        self._wrapped = AdminSiteClass()


site = DefaultMaterialAdminSite()
