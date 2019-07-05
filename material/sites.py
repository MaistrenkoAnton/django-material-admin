from django.contrib.admin.sites import AdminSite
from django.urls import NoReverseMatch, reverse
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string
from django.apps import apps
from django.utils.text import capfirst


class MaterialAdminSite(AdminSite):
    """Extends AdminSite to add material design for admin interface"""
    default_config_mapping = {
        'auth': 'group',
        'sites': 'web'
    }
    favicon = None

    def __init__(self, name='material'):
        super().__init__(name)
        self.login_template = 'material/login.html'
        self.logout_template = 'material/logout.html'
        self.index_template = 'material/index.html'
        self.password_change_template = 'material/password_change.html'

    def each_context(self, request):
        """Add favicon url to each context"""
        context = super().each_context(request)
        context['favicon'] = self.favicon
        return context

    def _build_app_dict(self, request, label=None):
        """
        Build the app dictionary. The optional `label` parameter filters models
        of a specific app. Adding material icons, default icons.
        """
        app_dict = {}

        if label:
            models = {
                m: m_a for m, m_a in self._registry.items()
                if m._meta.app_label == label
            }
        else:
            models = self._registry

        for model, model_admin in models.items():
            app_label = model._meta.app_label

            has_module_perms = model_admin.has_module_permission(request)
            if not has_module_perms:
                continue

            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True not in perms.values():
                continue

            info = (app_label, model._meta.model_name)
            model_dict = {
                'name': capfirst(model._meta.verbose_name_plural),
                'object_name': model._meta.object_name,
                'perms': perms,
                'icon': getattr(model_admin, 'icon_name', None)
            }
            if perms.get('change') or perms.get('view'):
                model_dict['view_only'] = not perms.get('change')
                try:
                    model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=self.name)
                except NoReverseMatch:
                    pass
            if perms.get('add'):
                try:
                    model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=self.name)
                except NoReverseMatch:
                    pass

            if app_label in app_dict:
                app_dict[app_label]['models'].append(model_dict)
            else:
                app_dict[app_label] = {
                    'name': apps.get_app_config(app_label).verbose_name,
                    'app_label': app_label,
                    'app_url': reverse(
                        'admin:app_list',
                        kwargs={'app_label': app_label},
                        current_app=self.name,
                    ),
                    'has_module_perms': has_module_perms,
                    'models': [model_dict],
                    'icon': getattr(apps.get_app_config(app_label), 'icon_name', None)
                    or self.default_config_mapping.get(app_label)
                }

        if label:
            return app_dict.get(label)
        return app_dict


class DefaultMaterialAdminSite(LazyObject):
    def _setup(self):
        AdminSiteClass = import_string(apps.get_app_config('material').default_site)
        self._wrapped = AdminSiteClass()


site = DefaultMaterialAdminSite()
