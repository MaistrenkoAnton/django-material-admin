from django.contrib import admin

from demo.documents.models import Document, Link
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin


class LinkInline(admin.TabularInline):
    model = Link
    extra = 0


@register(Document)
class CountryAdmin(MaterialModelAdmin):
    list_display = ('name', 'picture', 'file', 'text')
    icon_name = 'library_books'
    search_fields = ('name',)
    inlines = [LinkInline]
