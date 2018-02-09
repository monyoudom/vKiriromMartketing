# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class Posts(models.Model):
    class Meta:
        verbose_name_plural = 'Post'
    title = models.CharField(max_length= 100,default =1)
    decrib = models.CharField(max_length=200,default=1)
    detail = models.CharField(max_length= 2000,default=2 )
    post_cover = models.ImageField(upload_to='index/postcover')
    post_thumbnail = ImageSpecField(source='post_cover',
                                      processors=[ResizeToFill(1280, 720)],
                                      format='JPEG',
                                      options={'quality': 60})
    posts_date = models.DateField(auto_now=True,blank = True)
    def __unicode__(self):
        return str(self.title)


class Image(models.Model):
    class Meta:
        verbose_name_plural = 'Image'
    file = models.FileField('image', upload_to='index/images/',default =1)
    gallery = models.ForeignKey(Posts, related_name='images', blank=True, null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.filename
    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

    