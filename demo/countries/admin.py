from django.contrib import admin

from demo.countries.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass
