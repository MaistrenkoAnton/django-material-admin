from material.decorators import register
from material.options import MaterialModelAdmin

try:
    from django.contrib.sites.models import Site

    @register(Site)
    class MaterialSiteAdmin(MaterialModelAdmin):
        """Register Site model with material styles"""

except RuntimeError:
    pass

try:
    from django.contrib.auth.admin import UserAdmin, GroupAdmin
    from django.contrib.auth.models import User, Group


    @register(User)
    class MaterialUserAdmin(MaterialModelAdmin, UserAdmin):
        """Register User model with material styles"""


    @register(Group)
    class MaterialGroupAdmin(MaterialModelAdmin, GroupAdmin):
        """Register Group model with material styles"""

except RuntimeError:
    pass
