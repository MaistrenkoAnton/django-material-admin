from django.contrib import messages
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
                {'display': _('Night'), 'name': 'night'},
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
        save_action = request.POST.get('action')
        extra_kwargs['preview_theme'] = preview or save_action
        response = self.get(request, **extra_kwargs)
        if save_action:
            self.message_user(save_action)
            response.set_cookie('current_theme', save_action)
        return response

    def message_user(self, theme_name):
        message = _('The "{}" theme was saved successfully.'.format(theme_name.title()))
        messages.add_message(self.request, messages.SUCCESS, message, fail_silently=True)
