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
                {'display': _('Darcula'), 'name': 'darcula'},
                {'display': _('Dark'), 'name': 'dark'},
                {'display': _('Red'), 'name': 'red'},
                {'display': _('Green'), 'name': 'green'},
            ),
            **(self.extra_context or {})
        })
        return context
