from django.contrib.auth.models import User, Group


class AuthUser(User):
    class Meta:
        proxy = True
        app_label = 'authentication'


class AuthGroup(Group):
    class Meta:
        proxy = True
        app_label = 'authentication'
