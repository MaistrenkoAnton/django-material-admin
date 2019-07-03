from django.core.exceptions import AppRegistryNotReady

from material.decorators import register
from material.options import MaterialModelAdmin

try:
    from django.contrib.sites.models import Site

    @register(Site)
    class MaterialSiteAdmin(MaterialModelAdmin):
        """Register Site model with material styles"""
        icon_name = 'web'

except (RuntimeError, AppRegistryNotReady):
    pass

try:
    from django.contrib.auth.admin import UserAdmin, GroupAdmin
    from django.contrib.auth.models import User, Group


    @register(User)
    class MaterialUserAdmin(MaterialModelAdmin, UserAdmin):
        """Register User model with material styles"""
        add_form_template = 'admin/add_form.html'
        icon_name = 'person'


    @register(Group)
    class MaterialGroupAdmin(MaterialModelAdmin, GroupAdmin):
        """Register Group model with material styles"""
        icon_name = 'people'

except (RuntimeError, AppRegistryNotReady):
    pass
