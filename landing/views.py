# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from products.models import *
from .forms import *


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

    phone_images = products_images.filter(product__category_id=1)
    laptop_images = products_images.filter(product__category_id=2)
    product_categorys = ProductCategory.objects.filter(is_active=True)
    queryset= product_categorys.values()
    cat_list=[cat for cat in queryset]
    print cat_list
    cat_list_tmp = set()
    for i in cat_list:
        print i['name']
        cat_list_tmp.add(i['name'])
    for category in cat_list_tmp:
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__category__is_active=True,product__category__name=category)
    return render(request, "html/landing/index.html", locals())


def registration(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        sign_in_form = SignInForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            username = sign_up_form.cleaned_data.get('username')
            raw_password = sign_up_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('index')
        if sign_in_form.is_valid():
            sign_in_form.save()
            username = sign_in_form.cleaned_data.get('username')
            raw_password = sign_in_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('index')
    else:
        sign_up_form = SignUpForm()
        sign_in_form = SignInForm()

    return render(request, "html/landing/registration.html", locals(),
                  {'sign_up_form': sign_up_form, 'sign_in_form': sign_in_form})


def contacts(request):
    return render(request, "html/landing/contacts.html", locals())


def delivery(request):
    return render(request, "html/landing/delivery.html", locals())


from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return render(request, "html/landing/index.html", locals())