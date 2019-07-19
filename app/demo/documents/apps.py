from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DocumentsConfig(AppConfig):
    name = 'demo.documents'
    icon_name = 'library_books'
    verbose_name = _('Documents')
