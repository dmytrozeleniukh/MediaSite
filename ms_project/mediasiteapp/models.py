# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
	
	name = models.CharField(max_length=50)
	slug = models.SlugField()

	def __unicode__(self):
		return self.name

def generate_filename(instance, filename):
	filename = instance.slug + '.jpg'
	return "{0}/{1}".format(instance, filename)

class ArticleManager(models.Manager):

	def all(self, *args, **kwargs):
		return super(ArticleManager, self).get_queryset().filter(pk__in=[2])


class Article(models.Model):

	category = models.ForeignKey(Category)
	title = models.CharField(max_length=120)
	slug = models.SlugField()
	image = models.ImageField(upload_to = generate_filename, blank=True)
	content = models.TextField()
	likes = models.PositiveIntegerField(default=0)
	dislikes = models.PositiveIntegerField(default=0)
	objects = models.Manager()
	custom_manager = ArticleManager()

	def __unicode__(self):
		return self.title


class MyArticles(Article): #test

	class Meta:
		proxy = True