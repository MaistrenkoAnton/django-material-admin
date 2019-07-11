from demo.relations.models import Relation
from material.decorators import register
from material.options import MaterialModelAdmin


@register(Relation)
class RelationAdmin(MaterialModelAdmin):
    list_display = ('id', 'name')
    icon_name = 'layers'
    autocomplete_fields = ('documents',)
