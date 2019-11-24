# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import book, contacts

urlpatterns = [
    url(r'^$', book, name='city'),
    url(r'^customers/', contacts, name='cities'),
    url(r'^thankyou/', contacts, name='thankyou'),
]