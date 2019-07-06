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
    """Time input with material css styles"""
    template_name = 'material/widgets/time.html'


class MaterialAdminTextareaWidget(widgets.AdminTextareaWidget):
    """Textarea with material css styles"""

    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'materialize-textarea', **(attrs or {})})
