# -*- coding: utf-8 -*-

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

class SeoData(models.Model):
    title = models.CharField(max_length=255, verbose_name=_(u'Page title'), blank=True, null=True)
    keywords = models.TextField(verbose_name=_(u'Keywords'))
    description = models.TextField(verbose_name=_(u'Description'), blank=True, null=True)

    class Meta:
        abstract = True

class SeoObject(SeoData):
    content_type = models.ForeignKey(ContentType, editable=False)
    object_pk = models.PositiveIntegerField(editable=False)
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_pk")

    class Meta:
        verbose_name = _(u'SEO object')
        verbose_name_plural = _(u'SEO objects')

class SeoURL(SeoData):
    url = models.CharField(max_length=255, verbose_name=_(u'URL'), help_text=_(u'Or beginning URL part beginning and ending with "/"'))

    class Meta:
        verbose_name = _(u'SEO path')
        verbose_name_plural = _(u'SEO path')




