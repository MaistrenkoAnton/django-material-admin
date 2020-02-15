from daterangefilter.filters import FutureDateRangeFilter
from django.contrib.admin import ModelAdmin, register
from django import forms

from demo.periods.models import DateTimeModel, TimeModel, DateModel, Period1, Period2, Period3, Period4, Period5
from adminsortable2.admin import SortableAdminMixin

from material.admin.widgets import MaterialAdminTimeWidget, MaterialAdminDateWidget


class DateForm(forms.ModelForm):
    date = forms.DateField(
        widget=MaterialAdminDateWidget,
    )

    class Meta:
        model = DateModel
        fields = ['date']


@register(DateModel)
class DateModelAdmin(SortableAdminMixin, ModelAdmin):
    icon_name = 'insert_invitation'
    form = DateForm
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


class TimeForm(forms.ModelForm):
    time = forms.TimeField(
        widget=MaterialAdminTimeWidget,
    )

    class Meta:
        model = TimeModel
        fields = ['time']


@register(TimeModel)
class PersonAdmin(ModelAdmin):
    icon_name = 'access_time'
    form = TimeForm


@register(DateTimeModel)
class PersonAdmin(ModelAdmin):
    icon_name = 'linear_scale'


@register(Period1)
class Period1Admin(ModelAdmin):
    icon_name = 'access_time'


@register(Period2)
class Period2Admin(ModelAdmin):
    icon_name = 'access_time'


@register(Period3)
class Period3Admin(ModelAdmin):
    icon_name = 'access_time'


@register(Period4)
class Period4Admin(ModelAdmin):
    icon_name = 'access_time'


@register(Period5)
class Period5Admin(ModelAdmin):
    icon_name = 'access_time'