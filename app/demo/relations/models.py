from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Relation(models.Model):
    documents = models.ManyToManyField('documents.Document', verbose_name=_('Documents'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    image = models.ImageField(verbose_name=_('User Image'), null=True)
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    is_relation = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Relation')
        verbose_name_plural = _('Relations')
        db_table = 'relations'
        ordering = ('id',)
