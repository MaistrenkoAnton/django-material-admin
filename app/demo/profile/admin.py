from django.contrib import admin

from demo.profile.model import UserProfile
from demo.relations.models import Relation

from django.contrib.auth.models import User

from material.admin.admin import MaterialUserAdmin
from material.admin.decorators import register
from material.admin.sites import site

site.unregister(User)


class UserPictureInline(admin.TabularInline):
    model = UserProfile
    extra = 0


class UserRelationInline(admin.TabularInline):
    model = Relation
    extra = 0


@register(User)
class MaterialUserPictureAdmin(MaterialUserAdmin):
    """Register User model with material styles"""
    inlines = [UserPictureInline, UserRelationInline]

