from django.db import models
from django.utils.translation import gettext_lazy as _


class Document(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    picture = models.ImageField(_('Picture'))
    file = models.FileField(_('File'))
    text = models.TextField(_('Text'))
    url = models.URLField(_('Url'), null=True)

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
        db_table = 'documents'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Link(models.Model):
    url = models.URLField(_('Url'))
    document = models.ForeignKey('documents.Document', verbose_name=_('Document'), null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
        db_table = 'links'

    def __str__(self):
        return self.url
