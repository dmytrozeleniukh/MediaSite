# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from mediasiteapp.models import Category, Article

admin.site.register(Category)
admin.site.register(Article)
# Register your models here.
