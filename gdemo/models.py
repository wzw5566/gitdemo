from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='作者')
    title = models.CharField(max_length=200, verbose_name='标题')
    text = models.TextField(verbose_name='文章内容')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='创建日期')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='发布日期')



    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title


    class Meta:

        verbose_name = '文章'
        verbose_name_plural = verbose_name