from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from demo.countries.models import Country, Person, ProxyPerson


class PersonInline(admin.TabularInline):
    model = Person
    ordering = ('id',)
    extra = 0


@register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ('name', 'created', 'modified')
    inlines = [PersonInline]
    icon_name = 'location_city'
    search_fields = ('name',)
    fieldsets = (('Advanced options', {
        'classes': ('collapse',),
        'fields': (('name', 'created'), 'modified', 'time'),
    }),)


@register(Person)
class PersonAdmin(ModelAdmin):
    icon_name = 'people_outline'
    autocomplete_fields = ('user', 'nationality')


@register(ProxyPerson)
class PersonAdmin(ModelAdmin):
    icon_name = 'android'
    autocomplete_fields = ('user', 'nationality')

