from django.contrib.admin import AdminSite


class MaterialAdminSite(AdminSite):
    login_template = 'material_admin/login.html'


admin_site = MaterialAdminSite()
