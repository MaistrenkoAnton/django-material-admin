from daterangefilter.filters import FutureDateRangeFilter
from django.contrib.admin import ModelAdmin, register

from demo.periods.models import DateTimeModel, TimeModel, DateModel


@register(DateModel)
class DateModelAdmin(ModelAdmin):
    icon_name = 'insert_invitation'
    list_display = ('id', 'date',)
    list_editable = ['date', ]
    list_filter = [('date', FutureDateRangeFilter)]
    search_fields = (
        'date',
    )
    date_heirarchy = (
        'date',
    )


@register(TimeModel)
class PersonAdmin(ModelAdmin):
    icon_name = 'access_time'


@register(DateTimeModel)
class PersonAdmin(ModelAdmin):
    icon_name = 'linear_scale'
