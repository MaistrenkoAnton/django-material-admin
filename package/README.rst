# Django Material Design Admin

Quick start
-----------

1. Add "material.admin" and "material.admin.default" to your INSTALLED_APPS setting instead of "django.contrib.admin":

     .. code-block:: python

        INSTALLED_APPS = (
            'material',
            'material.admin',

            'django.contrib.auth',
            ...
        )


2. Include the material templates URLconf in your project urls.py like this:

    .. code-block:: python

        urlpatterns = [
            path('admin/', admin.site.urls),
        ]

3. Use the admin with material styles

    .. code-block:: python

        from django.contrib.admin import ModelAdmin, register

        from persons.models import Person


        @register(Person)
        class PersonAdmin(ModelAdmin):
            list_display = ('name', 'first_name', 'last_name')


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

        from django.contrib.admin import ModelAdmin, register
        from persons.models import Person


        @register(Person)
        class MaterialPersonAdmin(ModelAdmin):
            icon_name = 'person'
