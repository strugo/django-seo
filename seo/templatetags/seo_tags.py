# -*- coding: utf-8 -*-

from django import template
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.loader import render_to_string

from seo.models import SeoObject, SeoURL

register = template.Library()

@register.simple_tag
def seo_universal(obj, path):
    if obj and isinstance(obj, models.Model):
        try:
            return seo_object(obj)
        except SeoObject.DoesNotExist:
            pass
    return seo_url(path, obj)

def render_seo(seo, obj=None):
    return render_to_string(['custom_seo/tags.html', 'seo/tags.html'], {'seo': seo, 'obj': obj})

@register.simple_tag
def seo_object(obj):
    ct = ContentType.objects.get_for_model(obj)
    seo = SeoObject.objects.get(content_type=ct, object_pk=obj.pk)
    return render_seo(seo, obj)

@register.simple_tag
def seo_url(path, obj=None):
    bits = path.strip('/').split('/')
    for i in range(len(bits)+1):
        subpath = '/'.join(bits[:len(bits)-i])
        subpath = '/%s/' % subpath
        subpath = subpath.replace('//', '/')
        try:
            seo = SeoURL.objects.filter(url=subpath)[0]
        except IndexError:
            pass
        else:
            return render_seo(seo, obj=obj)
    return render_seo(None, obj=obj)
