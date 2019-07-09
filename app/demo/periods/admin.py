from django.contrib import admin

from demo.countries.models import Country, Person
from demo.periods.models import DateTimeModel, TimeModel, DateModel
from material.decorators import register
from material.options import MaterialModelAdmin


@register(DateModel)
class DateModelAdmin(MaterialModelAdmin):
    icon_name = 'insert_invitation'


@register(TimeModel)
class PersonAdmin(MaterialModelAdmin):
    icon_name = 'access_time'


@register(DateTimeModel)
class PersonAdmin(MaterialModelAdmin):
    icon_name = 'linear_scale'
