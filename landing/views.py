# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from products.models import *
from .forms import SubscriberForm


# Create your views here.

def landing(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        # print (request.POST)
        # print (form.cleaned_data)

        new_form = form.save()

    return render(request, "html/landing/landing.html", locals())


def index(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__category__is_active=True)
    phone_images=products_images.filter(product__category_id=1)
    laptop_images=products_images.filter(product__category_id=2)
    return render(request, "html/landing/index.html", locals())


