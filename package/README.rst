# Django Material Design Admin

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

        from persons.models import Person


        @register(Person)
        class PersonAdmin(MaterialModelAdmin):
            list_display = ('name', 'first_name', 'last_name')

    or

    .. code-block:: python

        from material.options import MaterialModelAdmin
        from material.sites import site

        from persons.models import Person


        class PersonAdmin(MaterialModelAdmin):
            list_display = ('name', 'first_name', 'last_name')

        site.register(User)

4. Add icon to the application in `app.py`
https://materializecss.com/icons.html

    .. code-block:: python

        from django.apps import AppConfig


        class PersonsConfig(AppConfig):
            name = 'persons'
            icon_name = 'person'


5. Add icon to the MaterialModelAdmin in `admin.py`
https://materializecss.com/icons.html

    .. code-block:: python

        from material.options import MaterialModelAdmin
        from material.decorators import register

        from persons.models import Person


        @register(Person)
        class MaterialPersonAdmin(MaterialModelAdmin):
            icon_name = 'person'
