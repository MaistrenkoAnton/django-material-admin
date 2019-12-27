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
    is_approved = models.BooleanField(_('Approved'), default=False)
    type = models.CharField(
        _('Type'),
        choices=(
            ('choice1', 'Choice1'),
            ('choice2', 'Choice2'),
            ('choice3', 'Choice3'),
            ('choice4', 'Choice4'),
            ('choice5', 'Choice5'),
            ('choice6', 'Choice6'),
            ('choice7', 'Choice7'),
            ('choice8', 'Choice8'),
            ('choice9', 'Choice9'),
            ('choice10', 'Choice10'),
            ('choice11', 'Choice11'),
        ),
        null=True,
        max_length=64
    )

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
        db_table = 'links'

    def __str__(self):
        return self.url
