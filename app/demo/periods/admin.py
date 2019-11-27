from daterangefilter.filters import FutureDateRangeFilter

from demo.periods.models import DateTimeModel, TimeModel, DateModel
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin


@register(DateModel)
class DateModelAdmin(MaterialModelAdmin):
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
class PersonAdmin(MaterialModelAdmin):
    icon_name = 'access_time'


@register(DateTimeModel)
class PersonAdmin(MaterialModelAdmin):
    icon_name = 'linear_scale'
