from django.contrib.admin.apps import AdminConfig


class DefaultMaterialConfig(AdminConfig):
    default_site = 'material.admin.sites.MaterialAdminSite'
