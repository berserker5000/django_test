# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CheckOut_contact_form
from .models import *


# Create your views here.

def basket_adding(request):
    return_dict = dict()

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")

    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                 defaults={"number": nmb})
    if not created:
        new_product.number += int(nmb)
        new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_number = products_in_basket.count()
    return_dict['products_total_number'] = products_total_number

    return_dict['products'] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict['item_product_name'] = item.product.product_name
        product_dict['price_per_item'] = item.price_per_item
        product_dict['number'] = item.number
        return_dict['products'].append(product_dict)
    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = CheckOut_contact_form(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            data = request.POST
            name = data['name']
            phone = data['phone']
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=4)

            for name, value in data.items():
                if name.startswith("product_id_"):
                    product_in_basket_id = name.split('product_id_')[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    product_in_basket.number = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)
                    ProductInOrder.objects.create(product=product_in_basket.product, number=product_in_basket.number,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  total_price=product_in_basket.total_price,
                                                  order=order)

            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            print "no"

    return render(request, "html/checkout.html", locals())