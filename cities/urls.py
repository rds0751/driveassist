# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import ContactView, contacts

urlpatterns = [
    url(r'^$', ContactView.as_view(), name='city'),
    url(r'^customers/', contacts, name='cities'),
    url(r'^thankyou/', contacts, name='thankyou'),
]
