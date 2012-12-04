from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from seo.models import SeoObject, SeoURL
from django.core.exceptions import ObjectDoesNotExist

class SeoObjectInline(GenericTabularInline):
    model = SeoObject
    extra = 1
    max_num = 1
    ct_field = "content_type"
    ct_fk_field = "object_pk"

class SeoURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'title')
    ordering = ['url', ]
    search_fields = ['url', 'title']
    fieldsets = (None, {
        'fields': ('title', 'url', 'description', 'keywords'),
    }),

admin.site.register(SeoURL, SeoURLAdmin)