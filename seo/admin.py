from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from apps.seo.models import SeoObject, SeoURL
from django.core.exceptions import ObjectDoesNotExist

class SeoObjectInline(GenericTabularInline):
    model = SeoObject
    extra = 0

    def queryset(self, request):
        qs = super(SeoObjectInline, self).queryset(request)
        try:
            qs.get()
        except ObjectDoesNotExist:
            self.extra = 1
        return qs

class SeoURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'title')
    ordering = ['url', ]
    search_fields = ['url', 'title']

admin.site.register(SeoURL, SeoURLAdmin)