from daterangefilter.filters import FutureDateRangeFilter
from django.contrib.admin import ModelAdmin, register

from demo.periods.models import DateTimeModel, TimeModel, DateModel
from adminsortable2.admin import SortableAdminMixin


@register(DateModel)
class DateModelAdmin(SortableAdminMixin, ModelAdmin):
    icon_name = 'insert_invitation'
    list_display = ('id', 'my_order', 'date')
    # ordering = ('my_order', )
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
