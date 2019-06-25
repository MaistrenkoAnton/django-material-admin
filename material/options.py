from django.contrib.admin.options import ModelAdmin
from django.db import models
from django.forms import SplitDateTimeField

from material import widgets

FORMFIELD_FOR_DBFIELD_MATERIAL = {
    models.DateField: {'widget': widgets.MaterialAdminDateWidget},
    models.DateTimeField: {
        'form_class': SplitDateTimeField,
        'widget': widgets.MaterialAdminSplitDateTime
    },
    models.TimeField: {'widget': widgets.MaterialAdminTimeWidget},
    models.ImageField: {'widget': widgets.MaterialAdminFileWidget},
    models.FileField: {'widget': widgets.MaterialAdminFileWidget},
}


class MaterialModelAdmin(ModelAdmin):
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.formfield_overrides.update(FORMFIELD_FOR_DBFIELD_MATERIAL)
