from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


class ThemesView(TemplateView):
    title = _('Theme selection')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'themes': (
                _('Default'),
                _('Darcula'),
                _('Dark'),
                _('Red'),
                _('Green'),
            ),
            **(self.extra_context or {})
        })
        return context
