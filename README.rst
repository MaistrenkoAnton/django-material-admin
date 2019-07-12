|pypi| |python| |django|


.. |pypi| image:: https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&type=6&v=1.1.18&x2=0
    :target: https://pypi.org/project/django-material-admin/
.. |python| image:: https://img.shields.io/badge/python-3.4+-blue.svg
    :target: https://www.python.org/
.. |django| image:: https://img.shields.io/badge/django-2.2-blue.svg
    :target: https://www.djangoproject.com/

==============================
Django Material Administration
==============================


.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/login.png


Demo version:
http://ec2-35-157-197-184.eu-central-1.compute.amazonaws.com/admin/


**login**: *admin*

**pass**: *123qaz123!A*

Quick start
-----------

 
**pip install django-material-admin**

1. Add "django-material-admin" to your INSTALLED_APPS setting like this:

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'material',
        'django.contrib.admin',
        ...,
    )


2. Include the material templates URLconf in your project urls.py like this:

.. code-block:: python

    from django.urls import path, include

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

    site.register(Person)


4. Add icon to the application in `app.py`
https://materializecss.com/icons.html

.. code-block:: python

    from django.apps import AppConfig


    class PersonsConfig(AppConfig):
        name = 'persons'
        icon_name = 'person'


5. Add icon to the MaterialModelAdmin in `admin.py`

.. code-block:: python

    from material.options import MaterialModelAdmin
    from material.decorators import register

    from persons.models import Person


    @register(Person)
    class MaterialPersonAdmin(MaterialModelAdmin):
        icon_name = 'person'






+++++++++++++++++
Planned features:
+++++++++++++++++

+++++++++++++++++
- Facets for apps
+++++++++++++++++


.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/facets_for_apps.png

++++++
- Tray
++++++

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/tray.png

++++++++++++++++
- Minimize tools
++++++++++++++++

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/tools-opened.jpg

+++++++++++++++++++
- Minimize Side Nav
+++++++++++++++++++

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/minimize-side-nav.png

++++++++++++++++++++++++++++++++++++++
- Additional Submit Row and Minimizing
++++++++++++++++++++++++++++++++++++++

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/addition-submit-line.png

+++++++++++++++++++++++++++++++++++
- Additional Facets/Badges for apps
+++++++++++++++++++++++++++++++++++

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/badges.jpg


+++++
- UTs
+++++

++++++++++++++++++++++++++++++++
- Check loading, refactor static
++++++++++++++++++++++++++++++++

++++++++++++++++++++++
- Material BreadCrumbs
++++++++++++++++++++++

++++++++++++++++++
- Themes selection
++++++++++++++++++

+++++++++++++++++++++++++++++++++++++
- Fixing issues, support new versions
+++++++++++++++++++++++++++++++++++++

++++++++++++++++++++++++++++++++++++++++
 - Materialize inline formset generation
++++++++++++++++++++++++++++++++++++++++
