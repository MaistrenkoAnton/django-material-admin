from django.urls import path

from material.admin.sites import site


urlpatterns = [
    path('', site.urls, name='base')
]
