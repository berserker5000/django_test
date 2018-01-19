# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
# class Subscriber(models.Model):
#     name = models.CharField(max_length=128)
#     email = models.EmailField()
#
#     def __str__(self):
#         try:
#             return self.name
#         except Exception:
#             return self.id




class ProductCategory(models.Model):
    name=models.CharField(max_length=128, default=None,blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" %self.name


class Product(models.Model):
    product_name = models.CharField(max_length=128, default=None)
    price=models.DecimalField(max_digits=10,decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True)
    short_description = models.TextField(max_length=200, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" %self.product_name



class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='static/product_images')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" %self.id

