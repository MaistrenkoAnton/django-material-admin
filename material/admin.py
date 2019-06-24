from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from material.options import MaterialModelAdmin


class AuthUser(User):
    class Meta:
        proxy = True
        app_label = 'auth'


class AuthGroup(Group):
    class Meta:
        proxy = True
        app_label = 'auth'


@admin.register(AuthUser)
class MaterialUserAdmin(MaterialModelAdmin, UserAdmin):
    pass


@admin.register(AuthGroup)
class MaterialGroupAdmin(MaterialModelAdmin, GroupAdmin):
    pass


admin.site.unregister(User)
admin.site.unregister(Group)
