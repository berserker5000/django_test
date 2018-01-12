# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.


# class SubscriberAdmin(admin.ModelAdmin):
#     # list_display = [field.name for field in Subscriber._meta.fields]
#     list_display = ["name",'email']
#     list_filter = ["name"]
#     search_fields = ["name", "email"]
#     class Meta:
#         model = Subscriber
#
#
# admin.site.register(Subscriber, SubscriberAdmin)



class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory,ProductCategoryAdmin)



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


admin.site.register(ProductImage,ProductImageAdmin)


class ProductAdmin(admin.ModelAdmin):
    exclude = ["id"]
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]


    class Meta:
        model = Product


admin.site.register(Product,ProductAdmin)