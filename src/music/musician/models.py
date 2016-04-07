# --*-- coding:utf-8 --*--
from django.db import models

# Create your models here.

class Musicians(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name=u'歌手名字')
    link_url = models.URLField(max_length=200, verbose_name=u'歌手信息链接')
    letter_index = models.CharField(max_length=10, verbose_name=u'歌手名字首字母')
    class Meta:
        ordering = ('letter_index',)