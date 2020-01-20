from django import forms

from demo.documents.forms import CachedMaterialAdminFileWidget
from demo.relations.models import Relation


class RelationForm(forms.ModelForm):
    image = forms.ImageField(widget=CachedMaterialAdminFileWidget)

    class Meta:
        model = Relation
        fields = '__all__'
