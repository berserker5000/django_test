from django.conf.urls import url
from django.contrib import admin
# from django.urls import path

from landing import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^registration', views.registration, name="registration"),
    url(r'^contacts', views.contacts, name="contacts"),
    url(r'^delivery', views.delivery, name="delivery"),
    url(r'^logout_view', views.logout_view, name="logout_view"),
]