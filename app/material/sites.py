from django.contrib.admin.sites import site

material_templates = {
    'login_template': 'material/login.html',
    'logout_template': 'material/logout.html',
    'index_template': 'material/index.html',
    'login_form': None,
    'app_index_template': None,
    'password_change_template': 'material/password_change.html',
    'password_change_done_template': None
}

site._wrapped.__dict__.update(material_templates)
material_site = site
