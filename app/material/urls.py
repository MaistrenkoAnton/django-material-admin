from django.urls import path

from material.sites import site


urlpatterns = [
    path('', site.urls, name='base')
]
