from django.contrib import admin

from demo.profile.model import UserProfile
from demo.relations.models import Relation
from material.admin import MaterialUserAdmin
from material.decorators import register
from material.sites import site

from django.contrib.auth.models import User


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

