from django import forms

from filefield_cache.widgets import CachedAdminFileWidget
from demo.documents.models import Document


class CachedMaterialAdminFileWidget(CachedAdminFileWidget):
    template_name = 'admin/widgets/clearable_file_input.html'


class DocumentForm(forms.ModelForm):
    file = forms.FileField(widget=CachedMaterialAdminFileWidget)
    picture = forms.ImageField(widget=CachedMaterialAdminFileWidget)

    class Meta:
        model = Document
        fields = '__all__'
