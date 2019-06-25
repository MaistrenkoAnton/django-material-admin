from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from material.authentication.models import AuthUser, AuthGroup
from material.options import MaterialModelAdmin


@admin.register(AuthUser)
class MaterialUserAdmin(MaterialModelAdmin, UserAdmin):
    pass


@admin.register(AuthGroup)
class MaterialGroupAdmin(MaterialModelAdmin, GroupAdmin):
    pass


admin.site.unregister(User)
admin.site.unregister(Group)
