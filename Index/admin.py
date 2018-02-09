# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiupload.admin import MultiUploadAdmin
from django.contrib import admin
from .models import Image,Posts

class ImageInlineAdmin(admin.TabularInline):
    model = Image
class PostMultiuploadMixing(object):
    def process_uploaded_file(self, uploaded, gallery, request):
        if gallery:
            image = gallery.images.create(file=uploaded)
        else:
            image = Image.objects.create(file=uploaded, gallery=None)
        return {
            'url': image.file.url,
            'thumbnail_url': image.file.url,
            'id': image.id,
            'name': image.filename
        }

class PostAdmin(PostMultiuploadMixing, MultiUploadAdmin):
    inlines = [ImageInlineAdmin,]
    multiupload_form = True
    multiupload_list = False

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Image, pk=pk)
        return obj.delete()
class ImageAdmin(PostMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
    multiupload_list = False
# Register your models here.
admin.site.register(Posts,PostAdmin)
#admin.site.register(Image,ImageAdmin)

