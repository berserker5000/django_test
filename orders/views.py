# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from .models import ProductInBasket

# from .forms import SubscriberForm


# Create your views here.

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


def basket_adding(request):
    return_dict=dict()

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    data=request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")

    new_product, created=ProductInBasket.objects.get_or_create(session_key=session_key,product_id=product_id,defaults={"number":nmb})
    if not created:
        new_product.number += int(nmb)
        new_product.save(force_update=True)



    products_in_basket=ProductInBasket.objects.filter(session_key=session_key,is_active=True)
    products_total_number=products_in_basket.count()
    return_dict['products_total_number'] = products_total_number

    return_dict['products'] = list()

    for item in products_in_basket:
        product_dict=dict()
        product_dict['item_product_name'] = item.product.product_name
        product_dict['price_per_item'] = item.price_per_item
        product_dict['number'] = item.number
        return_dict['products'].append(product_dict)

    # print (request.POST)
    return JsonResponse(return_dict)