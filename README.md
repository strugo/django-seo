django-seo
==========

You just need to add two lines:

    inlines = [SeoObjectInline] # in your admin.py
    {% seo_universal object request.path %} # inside your basic template's HEAD tag

This will take SEO attached to the object or path based data if object is empty