# -*- coding: utf-8 -*-

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

class SeoData(models.Model):
    title = models.CharField(verbose_name=_(u'Page title'), max_length=255, blank=True, null=True)
    keywords = models.TextField(verbose_name=_(u'Keywords'), blank=True, null=True)
    description = models.TextField(verbose_name=_(u'Description'), blank=True, null=True)
    og_title = models.CharField(verbose_name=_(u'Open Graph Title'), max_length=255, blank=True, null=True)
    og_description = models.TextField(verbose_name=_(u'Open Graph Description'), blank=True, null=True)
    og_image_url = models.URLField(verbose_name=_(u'Open Graph URL'), blank=True, null=True)

    class Meta:
        abstract = True

class SeoObject(SeoData):
    content_type = models.ForeignKey(ContentType, editable=False)
    object_pk = models.PositiveIntegerField(editable=False)
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_pk")

    class Meta:
        verbose_name = _(u'SEO object')
        verbose_name_plural = _(u'SEO objects')

class SeoURL(SeoData):
    url = models.CharField(max_length=255, verbose_name=_(u'URL'), help_text=_(u'Or beginning URL part beginning and ending with "/"'), unique=True)

    class Meta:
        verbose_name = _(u'SEO path')
        verbose_name_plural = _(u'SEO path')

    def clean(self):
        if self.url:
            if not self.url[0] == u'/':
                raise ValidationError('URL should begin with "/".')


class SeoMetaBase(models.Model):
    http_equiv = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    charset= models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True


class SeoURLMeta(SeoMetaBase):
    seo_url = models.ForeignKey(SeoURL, related_name='metatags')

    class Meta:
        verbose_name = _(u'SEO path metatag')
        verbose_name_plural = _(u'SEO path metatag')

    def __unicode__(self):
        return u'#%s %s' % (self.id, self.name,)

    @property
    def html_tag(self):
        dump = {}
        for field in self._meta.fields:
            if field.name in ('id', 'seo_url',):
                continue
            val = getattr(self, field.name, None)
            if val:
                dump.update({ field.name : val })
        if dump:
            out = [u'<meta']
            for name, data in dump.items():
                out.append(u'%s="%s"' % (name, data))
            out.append('>')
            return u' '.join(out)
        return u''

