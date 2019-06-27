from django.apps import AppConfig


class MaterialConfig(AppConfig):
    name = 'material'
    default_site = 'material.sites.MaterialAdminSite'
