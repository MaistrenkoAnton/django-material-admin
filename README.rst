|pypi| |python| |django|

|build|


.. |pypi| image:: https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&type=6&v=1.3.3&x2=0
    :target: https://pypi.org/project/django-material-admin/
.. |python| image:: https://img.shields.io/badge/python-3.4+-blue.svg
    :target: https://www.python.org/
.. |django| image:: https://img.shields.io/badge/django-2.2-blue.svg
    :target: https://www.djangoproject.com/    
.. |build| image:: http://ec2-35-157-197-184.eu-central-1.compute.amazonaws.com:8080/buildStatus/icon?job=Job1
    :target: http://ec2-35-157-197-184.eu-central-1.compute.amazonaws.com

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
 - required

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'material.admin',
        'django.contrib.admin',
        ...,
    )


2. Include the material templates URLconf in your project urls.py like this:
 - required

.. code-block:: python

    from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
    from django.utils.translation import ugettext_lazy as _

    from material.admin.sites import site

    site.site_header = _('Your site header')
    site.site_title = _('Your site title')
    site.favicon = staticfiles('path/to/favicon')


    urlpatterns = [
        path('admin/', include('material.admin.urls')),
    ]


3. Register your models and extend Admin config from  `MaterialModelAdmin`
 - optional

.. code-block:: python

    from material.admin.decorators import register
    from material.admin.options import MaterialModelAdmin


    from persons.models import Person

    @register(Person)
    class PersonAdmin(MaterialModelAdmin):
        list_display = ('name', 'first_name', 'last_name')

or

.. code-block:: python

    from material.admin.options import MaterialModelAdmin
    from material.admin.sites import site

    from persons.models import Person


    class PersonAdmin(MaterialModelAdmin):
        list_display = ('name', 'first_name', 'last_name')

    site.register(Person)

4. If you want to hide default registered models, they can be unregistered:
 - optional

.. code-block:: python

    from django.material.admin.sites import site
    from django.contrib.auth.models import User, Group

    site.unregister(User)
    site.unregister(Group)


5. Add icon to the application in `app.py`
https://materializecss.com/icons.html
 - optional

.. code-block:: python

    from django.apps import AppConfig


    class PersonsConfig(AppConfig):
        name = 'persons'
        icon_name = 'person'


6. Add icon to the MaterialModelAdmin in `admin.py`
 - optional

.. code-block:: python

    from material.admin.options import MaterialModelAdmin
    from material.admin.decorators import register

    from persons.models import Person


    @register(Person)
    class MaterialPersonAdmin(MaterialModelAdmin):
        icon_name = 'person'


7. In order to add and manage the profile picture, this template can be added.  
 - optional

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/django-material-admin/master/app/demo/screens/profile-pic.png

Extend **User** model as OneToOne relation or extend **AbstractUser** and set new **AUTH_USER_MODEL**.

**MEDIA** should be configured properly.

Then define template **templates/profile/user_picture.html** in any your application as example:

.. code-block:: python

    {% load static %}

    {% if user.profile.picture %}
        <a href="{% url 'admin:auth_user_change' user.pk %}">
            <img class="login-logo" src="{{ user.profile.picture.url }}">
        </a>
    {% else %}
        <img class="login-logo" src="{% static 'material/admin/images/login-logo.png' %}">
    {% endif %}
    <img src="{% static 'material/admin/images/login-bg.jpg' %}">
    <div class="card-title">
        <strong>{% firstof user.get_short_name user.get_username %}</strong>
        <small>{{ user.email|default_if_none:'' }}</small>
    </div>


Where 
 - *user.profile.picture* - the relation to ImageField from user,
 - *material/admin/images/login-logo.png* - default logo from material templates.
