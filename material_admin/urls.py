from django.contrib import admin
from django.urls import path
from material_admin.views import admin_site

urlpatterns = [
    path('login/', admin_site.login, name='login'),
    path('logout/', admin_site.logout, name='logout'),
    path('', admin.site.urls),
]
