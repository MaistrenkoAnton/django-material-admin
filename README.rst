# Django Material Admin

Coming soon...

Quick start
-----------

1. Add "django-material-admin" to your INSTALLED_APPS setting like this::

.. code:: python

    INSTALLED_APPS = (
        ...
        'django-material-admin',
        'django.contrib.admin',
    )


2. Include the material templates URLconf in your project urls.py like this::

.. code:: python
    path('admin/', include('material_admin.urls')),


