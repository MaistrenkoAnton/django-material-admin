from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from material.options import MaterialModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class MaterialUserAdmin(MaterialModelAdmin, UserAdmin):
    """Register User model with material styles"""


@admin.register(Group)
class MaterialGroupAdmin(MaterialModelAdmin, GroupAdmin):
    """Register Group model with material styles"""
