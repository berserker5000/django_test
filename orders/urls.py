from django.conf.urls import url
from django.contrib import admin
# from django.urls import path

from landing import views

admin.autodiscover()

urlpatterns = [
    # url(r'^', views.index, name="index"),
]