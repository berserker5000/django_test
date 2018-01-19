# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *



class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]
    exclude = ["id"]
    list_filter = ["status"]
    search_fields = ["status", "customer name"]

    class Meta:
        model = Order


admin.site.register(Order,OrderAdmin)

class StausAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status,StausAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]


    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder,ProductInOrderAdmin)




class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]


    class Meta:
        model = ProductInBasket


admin.site.register(ProductInBasket,ProductInBasketAdmin)