from django.contrib.admin import site as admin_site
from django.urls import path

admin_site.login_template = 'material_admin/login.html'
admin_site.logout_template = 'material_admin/logout.html'
admin_site.index_template = 'material_admin/index.html'

urlpatterns = [
    path('', admin_site.urls),
]
