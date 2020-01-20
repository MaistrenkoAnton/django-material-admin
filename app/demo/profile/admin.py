from django.contrib import admin, messages
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from demo.profile.forms import RelationForm
from demo.profile.models import UserProfile
from demo.relations.models import Relation

from django.contrib.auth.models import User


class UserPictureInline(admin.TabularInline):
    model = UserProfile
    extra = 0


class UserRelationInline(admin.StackedInline):
    model = Relation
    form = RelationForm
    extra = 0


admin.site.unregister(User)


@register(User)
class MaterialUserPictureAdmin(UserAdmin):
    """Register User model with material styles"""
    icon_name = 'person'
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

