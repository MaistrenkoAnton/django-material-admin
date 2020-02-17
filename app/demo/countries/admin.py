from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from modeltranslation.admin import TranslationAdmin

from demo.countries.models import Country, Person, ProxyPerson, Country1, Country2, Country3, Country4, Country5, Country6


class PersonInline(admin.TabularInline):
    model = Person
    ordering = ('id',)
    extra = 3
    fields = ('uuid', 'date', 'video', 'time')


@register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = ('name', 'created', 'modified')
    inlines = [PersonInline]
    icon_name = 'location_city'
    search_fields = ('name',)
    date_hierarchy = 'created'
    list_filter = ('name',)

    # def has_add_permission(self, obj):
    #     return False

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

    # fieldsets = (('Advanced options', {
    #     'classes': ('collapse',),
    #     'fields': (('name', 'created'), 'modified', 'time'),
    # }),)


@register(Person)
class PersonAdmin(ModelAdmin):
    icon_name = 'people_outline'
    autocomplete_fields = ('user', 'nationality')


@register(ProxyPerson)
class PersonAdmin(ModelAdmin):
    icon_name = 'android'
    autocomplete_fields = ('user', 'nationality')


@register(Country1)
class PersonAdmin(ModelAdmin):
    pass


@register(Country2)
class PersonAdmin(ModelAdmin):
    pass


@register(Country3)
class PersonAdmin(ModelAdmin):
    pass


@register(Country4)
class PersonAdmin(ModelAdmin):
    pass


@register(Country5)
class PersonAdmin(ModelAdmin):
    pass


@register(Country6)
class PersonAdmin(ModelAdmin):
    pass
