# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Subscriber._meta.fields]
    list_display = ["name",'email']
    list_filter = ["name"]
    search_fields = ["name", "email"]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)


#
# class SignInAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in SignIn._meta.fields]
#     class Meta:
#         model = SignIn
#
#
# admin.site.register(SignIn, SignInAdmin)