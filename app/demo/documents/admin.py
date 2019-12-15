from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from demo.documents.models import Document, Link


class LinkInline(admin.TabularInline):
    model = Link
    extra = 0


@register(Document)
class CountryAdmin(ModelAdmin):
    list_display = ('name', 'picture', 'file', 'text')
    icon_name = 'library_books'
    search_fields = ('name',)
    inlines = [LinkInline]

