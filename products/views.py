# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from products.models import *


# from .forms import SubscriberForm
#
#
# # Create your views here.
#
# def index(request):
#     form = SubscriberForm(request.POST or None)
#
#     if request.method == "POST" and form.is_valid():
#         # print (request.POST)
#         # print (form.cleaned_data)
#
#         new_form = form.save()
#
#     return render(request, "html/index.html", locals())



def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print (request.session.session_key)


    return render(request, "html/products/product.html", locals())