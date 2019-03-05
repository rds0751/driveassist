# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import ContactView, contacts, BookView

urlpatterns = [
    url(r'^fill-new-location/$', ContactView.as_view(), name='city'),
    url(r'^unipoles/', contacts, name='cities'),
    url(r'^bid-now/', BookView.as_view(), name='book'),
]
