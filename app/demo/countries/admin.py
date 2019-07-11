from django.contrib import admin

from demo.countries.models import Country, Person
from material.decorators import register
from material.options import MaterialModelAdmin


class PersonInline(admin.StackedInline):
    model = Person
    ordering = ('id',)
    extra = 0


@register(Country)
class CountryAdmin(MaterialModelAdmin):
    list_display = ('name', 'created', 'modified')
    inlines = [PersonInline]
    icon_name = 'location_city'
    search_fields = ('name',)


@register(Person)
class PersonAdmin(MaterialModelAdmin):
    icon_name = 'people_outline'
    autocomplete_fields = ('user', 'nationality')

