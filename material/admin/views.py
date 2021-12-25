import datetime

from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class ThemesView(TemplateView):
    title = _('Theme selection')
    themes = (
        {'display': _('Default'), 'name': 'default'},
        {'display': _('Night'), 'name': 'night'},
        {'display': _('Black'), 'name': 'black'},
        {'display': _('Red'), 'name': 'red'},
        {'display': _('Green'), 'name': 'green'}
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'themes': self.themes,
            **(self.extra_context or {})
        })
        return context

    def post(self, request, *args, **kwargs):
        extra_kwargs = {}
        preview = request.POST.get('preview')
        save_action = request.POST.get('action')
        extra_kwargs['preview_theme'] = preview or save_action
        response = self.get(request, **extra_kwargs)
        if save_action:
            self.message_user(save_action)
            expires = datetime.datetime.now() + datetime.timedelta(days=365)
            response.set_cookie(key='current_theme', value=save_action, expires=expires)
        return response

    def message_user(self, theme_name):
        message = _('The "{}" theme was saved successfully.')
        messages.add_message(
            self.request, messages.SUCCESS,
            message.format(self._get_theme_display(theme_name)),
            fail_silently=True
        )

    def _get_theme_display(self, theme_name):
        themes = [theme['display'] for theme in self.themes if theme['name'] == theme_name]
        if themes:
            return themes[0]
        return _('Default')
