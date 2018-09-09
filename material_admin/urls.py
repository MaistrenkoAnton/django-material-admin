from django.contrib import admin
from django.urls import path
from material_admin.views import admin_site

urlpatterns = [
    path('login/', admin_site.login, name='login'),
    path('', admin.site.urls),
]
