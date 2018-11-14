# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    return "{0}/{1}".format(instance, filename)



class Article(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    image = models.ImageField(upload_to = generate_filename, blank=True)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    comments = GenericRelation('comments')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'category': self.category.slug,'slug': self.slug})


class MyArticles(Article): #test

    class Meta:
        proxy = True


class Comments(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    comments = models.TextField()
    time = models.DateTimeField(auto_now_add = True, auto_now = False)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')