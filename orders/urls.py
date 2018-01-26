from django.conf.urls import url
from django.contrib import admin
# from django.urls import path

from orders import views

admin.autodiscover()

urlpatterns = [
     url(r'^basket_adding/$', views.basket_adding, name="basket_adding"),
     url(r'^checkout/$', views.checkout, name="checkout"),
]