from django.urls import path

from material_admin.sites import material_site


urlpatterns = [
    path('', material_site.urls)
]
