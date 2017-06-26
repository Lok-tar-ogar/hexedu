from django.contrib import admin
from core.models import *


class NewsAdmin(admin.ModelAdmin):

    class Media:
        js = (
            '/static/js/tinymce/tinymce.min.js',
            '/static/js/tinymce/config.js',
        )
admin.site.register(Message)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(NewsImg)
admin.site.register(News, NewsAdmin)