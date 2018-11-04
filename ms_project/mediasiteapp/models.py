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


class Article(models.Model):

	category = models.ForeignKey(Category)
	title = models.CharField(max_length=120)
	slug = models.SlugField()
	image = models.ImageField(upload_to = generate_filename)
	content = models.TextField()
	likes = models.PositiveIntegerField(default=0)
	dislikes = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.title