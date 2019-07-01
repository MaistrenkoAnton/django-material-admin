## Django Material Administration

![Layout](https://github.com/MaistrenkoAnton/django-material-admin/blob/master/app/demo/screens/login.png)


Demo version:
http://ec2-35-157-197-184.eu-central-1.compute.amazonaws.com/admin/

###### login: admin
###### pass: 123qaz123!A

Quick start
-----------

###pip install django-material-admin

1. Add "django-material-admin" to your INSTALLED_APPS setting like this:

```python

INSTALLED_APPS = (
    ...,
    'material',
    'django.contrib.admin',
    ...,
)
```


2. Include the material templates URLconf in your project urls.py like this:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', include('material.urls')),
]
```

3. Extend Admin config from  `MaterialModelAdmin`

```python
from material.options import MaterialModelAdmin
from material.decorators import register

from persons.models import Person

@register(Person)
class PersonAdmin(MaterialModelAdmin):
    list_display = ('name', 'first_name', 'last_name')
```
    or
    
```python
from material.options import MaterialModelAdmin
from material.sites import site

from persons.models import Person


class PersonAdmin(MaterialModelAdmin):
    list_display = ('name', 'first_name', 'last_name')

site.register(Person)
 ```

4. Add icon to the application in `app.py`
https://materializecss.com/icons.html

```python
from django.apps import AppConfig


class PersonsConfig(AppConfig):
    name = 'persons'
    icon_name = 'person'
```
