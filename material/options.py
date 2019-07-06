from django.conf import settings
from django.contrib.admin.options import ModelAdmin
from django.db import models
from django.forms import SplitDateTimeField, forms

from material import widgets

FORMFIELD_FOR_DBFIELD_MATERIAL = {
    models.DateField: {'widget': widgets.MaterialAdminDateWidget},
    models.DateTimeField: {
        'form_class': SplitDateTimeField,
        'widget': widgets.MaterialAdminSplitDateTime
    },
    models.TimeField: {'widget': widgets.MaterialAdminTimeWidget},
    models.TextField: {'widget': widgets.MaterialAdminTextareaWidget},
}


class MaterialModelAdmin(ModelAdmin):
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.formfield_overrides.update(FORMFIELD_FOR_DBFIELD_MATERIAL)

    @property
    def media(self):
        extra = '' if settings.DEBUG else '.min'
        js = [
            'vendor/jquery/jquery%s.js' % extra,
            'jquery.init.js',
            'core.js',
            'actions%s.js' % extra,
            'urlify.js',
            'prepopulate%s.js' % extra,
            'vendor/xregexp/xregexp%s.js' % extra,
        ]
        material_js = [
            'material/js/RelatedObjectLookups.min.js',
        ]
        return forms.Media(js=['admin/js/%s' % url for url in js] + material_js)
