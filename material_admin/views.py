from django.contrib.admin import AdminSite


class MaterialAdminSite(AdminSite):
    login_template = 'material_admin/login.html'
    logout_template = 'material_admin/logout.html'


admin_site = MaterialAdminSite()
