from demo.documents.models import Document
from material.decorators import register
from material.options import MaterialModelAdmin


@register(Document)
class CountryAdmin(MaterialModelAdmin):
    list_display = ('name', 'picture', 'file', 'text')
    icon_name = 'library_books'
