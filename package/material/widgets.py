from django.contrib.admin import widgets
from django import forms


class MaterialAdminDateWidget(widgets.AdminDateWidget):
    """Date widget with material specific styling"""
    template_name = 'material/widgets/date.html'


class MaterialAdminSplitDateTime(forms.SplitDateTimeWidget):
    """A SplitDateTime Widget with material specific styling"""
    template_name = 'material/widgets/split_datetime.html'

    def __init__(self, attrs=None, date_format=None, time_format=None, date_attrs=None, time_attrs=None):
        date_attrs = date_attrs or {}
        date_attrs.update({'class': 'datepicker'})
        time_attrs = time_attrs or {}
        time_attrs.update({'class': 'timepicker'})
        super().__init__(attrs, date_format, time_format, date_attrs, time_attrs)


class MaterialAdminTimeWidget(forms.TimeInput):
    template_name = 'material/widgets/time.html'


class MaterialAdminFileWidget(widgets.AdminFileWidget):
    template_name = 'material/widgets/clearable_file_input.html'
