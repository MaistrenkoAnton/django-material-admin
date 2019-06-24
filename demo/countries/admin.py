from django.contrib import admin

from demo.countries.models import Country
from material.options import MaterialModelAdmin


@admin.register(Country)
class CountryAdmin(MaterialModelAdmin):
    list_display = ('name', 'created', 'modified')
