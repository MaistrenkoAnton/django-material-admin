from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

from material.decorators import register
from material.options import MaterialModelAdmin


@register(User)
class MaterialUserAdmin(MaterialModelAdmin, UserAdmin):
    """Register User model with material styles"""


@register(Group)
class MaterialGroupAdmin(MaterialModelAdmin, GroupAdmin):
    """Register Group model with material styles"""


@register(Site)
class MaterialSiteAdmin(MaterialModelAdmin):
    """Register Site model with material styles"""
