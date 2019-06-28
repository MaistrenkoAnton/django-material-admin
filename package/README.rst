# Django Material Admin

Coming soon...

Quick start
-----------

1. Add "django-material-admin" to your INSTALLED_APPS setting like this:

     .. code-block:: python

        INSTALLED_APPS = (
            ...
            'material',
            'django.contrib.admin',
            ...
        )


2. Include the material templates URLconf in your project urls.py like this:

    .. code-block:: python

        urlpatterns = [
            path('admin/', include('material.urls')),
        ]

3. Extend Admin config from  `MaterialModelAdmin`

    .. code-block:: python

        from material.options import MaterialModelAdmin
        from material.decorators import register

        @register(Person)
        class PersonAdmin(MaterialModelAdmin):
            list_display = ('name', 'first_name', 'last_name')

    or

    .. code-block:: python

        from material.options import MaterialModelAdmin
        from material.sites import site

        class PersonAdmin(MaterialModelAdmin):
            list_display = ('name', 'first_name', 'last_name')

        site.register(User)
