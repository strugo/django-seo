from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline

from seo.models import SeoObject, SeoURL, SeoURLMeta
from django.core.exceptions import ObjectDoesNotExist

class SeoObjectInline(GenericStackedInline):
    model = SeoObject
    extra = 1
    max_num = 1
    ct_field = "content_type"
    ct_fk_field = "object_pk"


class SeoMetaUrlInline(admin.TabularInline):
    model = SeoURLMeta


class SeoURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'title')
    ordering = ['url', ]
    search_fields = ['url', 'title']
    fieldsets = (None, {
        'fields': ('title', 'url', 'description', 'keywords', 'og_title', 'og_description', 'og_image_url',),
    }),
    inlines = [
        SeoMetaUrlInline,
    ]

admin.site.register(SeoURL, SeoURLAdmin)