from django.contrib.admin.sites import AdminSite
from django.urls import NoReverseMatch, reverse, path
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string
from django.apps import apps
from django.utils.text import capfirst

from material.admin.options import MaterialModelAdminMixin
from material.admin.settings import MATERIAL_ADMIN_SITE
from material.admin.views import ThemesView


class MaterialAdminSite(AdminSite):
    """Extends AdminSite to add material design for admin interface"""
    favicon = None
    main_bg_color = None
    main_hover_color = None
    profile_picture = None
    profile_bg = None
    login_logo = None
    logout_bg = None
    show_themes = False
    show_counts = False

    def register(self, model_or_iterable, admin_class=None, **options):
        if admin_class:
            admin_class = type('admin_class', (MaterialModelAdminMixin, admin_class), {})
        return super().register(model_or_iterable, admin_class, **options)

    def __init__(self, name='material'):
        super().__init__(name)
        self.login_template = 'material/admin/login.html'
        self.logout_template = 'material/admin/logout.html'
        self.index_template = 'material/admin/index.html'
        self.password_change_template = 'material/admin/password_change.html'
        self.theme_template = 'material/admin/theme_change.html'
        self.site_header = MATERIAL_ADMIN_SITE['HEADER'] or self.site_header
        self.site_title = MATERIAL_ADMIN_SITE['TITLE'] or self.site_title
        self.favicon = self.favicon or MATERIAL_ADMIN_SITE['FAVICON']
        self.main_bg_color = self.main_bg_color or MATERIAL_ADMIN_SITE['MAIN_BG_COLOR']
        self.main_hover_color = self.main_hover_color or MATERIAL_ADMIN_SITE['MAIN_HOVER_COLOR']
        self.profile_picture = self.profile_picture or MATERIAL_ADMIN_SITE['PROFILE_PICTURE']
        self.profile_bg = self.profile_bg or MATERIAL_ADMIN_SITE['PROFILE_BG']
        self.login_logo = self.login_logo or MATERIAL_ADMIN_SITE['LOGIN_LOGO']
        self.logout_bg = self.logout_bg or MATERIAL_ADMIN_SITE['LOGOUT_BG']
        self.show_themes = self.show_themes or MATERIAL_ADMIN_SITE['SHOW_THEMES']
        self.show_counts = self.show_counts or MATERIAL_ADMIN_SITE['SHOW_COUNTS']

    def get_urls(self):
        urls = super().get_urls()
        return urls[:-1] + [path('themes/', self.theme_change, name='themes')] + [urls[-1]]

    def theme_change(self, request, extra_context=None):
        """
        Handle the "change theme"
        """
        defaults = {
            'extra_context': {**self.each_context(request), **(extra_context or {})},
        }
        if self.theme_template is not None:
            defaults['template_name'] = self.theme_template
        request.current_app = self.name
        return ThemesView.as_view(**defaults)(request)

    def each_context(self, request):
        """Add favicon url to each context"""
        context = super().each_context(request)
        context['favicon'] = self.favicon
        context['main_bg_color'] = self.main_bg_color
        context['main_hover_color'] = self.main_hover_color
        context['profile_picture'] = self.profile_picture
        context['profile_bg'] = self.profile_bg
        context['login_logo'] = self.login_logo
        context['logout_bg'] = self.logout_bg
        context['show_themes'] = self.show_themes
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
            default_model_icons = MATERIAL_ADMIN_SITE['MODEL_ICONS'].get(model._meta.model_name)
            icon = getattr(model_admin, 'icon_name', default_model_icons)
            model_dict = {
                'name': capfirst(model._meta.verbose_name_plural),
                'object_name': model._meta.object_name,
                'perms': perms,
                'proxy': getattr(model, 'proxy', False),
                'count': model_admin.get_queryset(request).count() if self.show_counts else None,
                'icon': icon
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
                    or MATERIAL_ADMIN_SITE['APP_ICONS'].get(app_label)
                }

        if label:
            return app_dict.get(label)
        return app_dict


class DefaultMaterialAdminSite(LazyObject):
    def _setup(self):
        AdminSiteClass = import_string(apps.get_app_config('material.admin').default_site)
        self._wrapped = AdminSiteClass()


site = DefaultMaterialAdminSite()
