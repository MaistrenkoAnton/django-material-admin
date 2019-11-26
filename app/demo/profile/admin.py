from django.contrib import admin, messages

from demo.profile.models import UserProfile
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
    list_display = ('username', 'is_active', 'is_staff')
    actions = ['make_published']
    list_editable = ['is_staff']
    list_filter = ('date_joined',)

    def make_published(self, request, queryset):
        self.message_user(request, "Published INFO.")
        self.message_user(request, "Published ERROR.", messages.ERROR)
        self.message_user(request, "Published SUCCESS.", messages.SUCCESS)
        self.message_user(request, "Published WARNING.", messages.WARNING)

    make_published.short_description = "Mark selected stories as published"

