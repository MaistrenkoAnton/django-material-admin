from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


class ThemesView(TemplateView):
    title = _('Theme selection')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'themes': (
                {'display': _('Default'), 'name': 'default'},
                {'display': _('Dark'), 'name': 'dark'},
                {'display': _('Black'), 'name': 'black'},
                {'display': _('Red'), 'name': 'red'},
                {'display': _('Green'), 'name': 'green'},
            ),
            **(self.extra_context or {})
        })
        return context

    def post(self, request, *args, **kwargs):
        extra_kwargs = {}
        preview = request.POST.get('preview')
        if preview:
            extra_kwargs['preview_theme'] = preview
        response = self.get(request, **extra_kwargs)
        save_action = request.POST.get('action')
        if save_action:
            response.set_cookie('current_theme', save_action)
        return response
