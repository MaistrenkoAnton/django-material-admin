from demo.relations.models import Relation
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin


@register(Relation)
class RelationAdmin(MaterialModelAdmin):
    list_display = ('id', 'name')
    icon_name = 'layers'
    autocomplete_fields = ('documents', 'user')
