from django.urls import path

from material.sites import material_site


urlpatterns = [
    path('', material_site.urls, name='base')
]
