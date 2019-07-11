from django.db import models
from django.utils.translation import gettext_lazy as _


class Document(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    picture = models.ImageField(_('Picture'))
    file = models.FileField(_('File'))
    text = models.TextField()

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
        db_table = 'documents'
        ordering = ('name',)

    def __str__(self):
        return self.name
