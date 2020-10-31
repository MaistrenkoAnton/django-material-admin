|pypi| |python| |django|

.. .. |build|


.. |pypi| image:: https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&type=6&v=1.7.15&x2=0
    :target: https://pypi.org/project/django-material-admin/
.. |python| image:: https://img.shields.io/badge/python-3.4+-blue.svg
    :target: https://www.python.org/
.. |django| image:: https://img.shields.io/badge/django-2.2+|3.1-mediumseagreen.svg
    :target: https://www.djangoproject.com/ 
.. .. |build| image:: http://ec2-35-157-197-184.eu-central-1.compute.amazonaws.com:8080/buildStatus/icon?job=Job1
..    :target: http://ec2-35-157-197-184.eu-central-1.compute.amazonaws.com

==============================
Django Material Administration
==============================


.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/login.png

.. **login**: *admin*

.. **pass**: *123qaz123!A*

Quick start
-----------

 
**pip install django-material-admin**

1. Add **material.admin** and **material.admin.default** to your INSTALLED_APPS setting instead of **django.contrib.admin**::
 - required

.. code-block:: python

    INSTALLED_APPS = (
        'material.admin',
        'material.admin.default',

        'django.contrib.auth',
        ...
    )


2. Include the material templates URLconf in your project **urls.py** like this:
 - required
.. code-block:: python

    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
    ]


3. Register your models in **admin.py**.
  
.. code-block:: python

    from django.contrib.admin import ModelAdmin, register


    from persons.models import Person

    @register(Person)
    class PersonAdmin(ModelAdmin):
        list_display = ('name', 'first_name', 'last_name')

4. Add icon to the application in **app.py** and specify the app usage in **__init__.py**

https://materializecss.com/icons.html
 - optional
 
**__init.py__**

.. code-block:: python
    
    default_app_config = 'persons.apps.PersonsConfig'
    
**apps.py**

.. code-block:: python

    from django.apps import AppConfig


    class PersonsConfig(AppConfig):
        name = 'persons'
        icon_name = 'person'


5. Add icon to the MaterialModelAdmin in **admin.py**

Material icon's name sources:

https://materializecss.com/icons.html

https://material.io/resources/icons/?style=baseline

 - optional

.. code-block:: python

    from django.contrib.admin import ModelAdmin, register

    from persons.models import Person


    @register(Person)
    class MaterialPersonAdmin(ModelAdmin):
        icon_name = 'person'


6. Add Admin site configurations to **settings.py** file:

 - optional
##########################################################

.. code-block:: python

    MATERIAL_ADMIN_SITE = {
        'HEADER':  _('Your site header'),  # Admin site header
        'TITLE':  _('Your site title'),  # Admin site title
        'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
        'MAIN_BG_COLOR':  'color',  # Admin site main color, css color should be specified
        'MAIN_HOVER_COLOR':  'color',  # Admin site main hover color, css color should be specified
        'PROFILE_PICTURE':  'path/to/image',  # Admin site profile picture (path to static should be specified)
        'PROFILE_BG':  'path/to/image',  # Admin site profile background (path to static should be specified)
        'LOGIN_LOGO':  'path/to/image',  # Admin site logo on login page (path to static should be specified)
        'LOGOUT_BG':  'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
        'SHOW_THEMES':  True,  #  Show default admin themes button
        'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
        'NAVBAR_REVERSE': True,  # Hide side navbar by default
        'SHOW_COUNTS': True, # Show instances counts for each model
        'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
            'sites': 'send',
        },
        'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
            'site': 'contact_mail',
        }
    }
##########################################################




==================
Video instructions (DEPRECATED) #  will be updated soon
==================
|
|
- Install Django

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/material1.png
   :target: https://youtu.be/G101hR6gkFo
|
|
- Install Django-material-admin

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/material2.png
   :target: https://youtu.be/s0gi1CV5PZ0
|
|
- Register models for material administration interface

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/material3.png
   :target: https://youtu.be/C8AxT5RMnAw

