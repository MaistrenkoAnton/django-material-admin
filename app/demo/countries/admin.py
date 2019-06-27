from django.contrib import admin

from demo.countries.models import Country, Person
from material.decorators import register
from material.options import MaterialModelAdmin


class PersonInline(admin.TabularInline):
    model = Person
    ordering = ('id',)
    extra = 0


@register(Country)
class CountryAdmin(MaterialModelAdmin):
    list_display = ('name', 'created', 'modified')
    inlines = [PersonInline]


@register(Person)
class PersonAdmin(MaterialModelAdmin):
    pass
