from django.apps import AppConfig


class MaterialConfig(AppConfig):
    name = 'material.admin'
    label = 'material.admin'
    default_site = 'material.admin.sites.MaterialAdminSite'

