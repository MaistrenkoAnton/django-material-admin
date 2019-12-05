from django.contrib.admin import register, ModelAdmin
from django.core.exceptions import PermissionDenied
from django.template.response import TemplateResponse
from django.urls import path

from material.dashboard.models import Page


@register(Page)
class PageAdmin(ModelAdmin):
    icon_name = 'notifications_active'
    page_template = 'pages/page.html'

    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.model_name
        return [
            path('', self.page_view, name='%s_%s_changelist' % info),
        ]

    def page_view(self, request):
        self._check_permissions(request)
        context = self._get_context(request)
        return TemplateResponse(request, self.page_template, context)

    def _check_permissions(self, request):
        if not self.has_view_or_change_permission(request):
            raise PermissionDenied

    def _get_context(self, request):
        return dict(
            self.admin_site.each_context(request),
            title='Page',
        )
