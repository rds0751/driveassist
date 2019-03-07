# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^digital-marketing-company-punjab$', views.digi, name='digi'),
    url(r'^seo-company-in-punjab$', views.seo, name='seo'),
    url(r'^smo-company-in-punjab$', views.smo, name='smo'),
    url(r'^ppc-Company-in- Punjab$', views.ppc, name='ppc'),
    url(r'^website-design-and-development$', views.web, name='web'),
    url(r'^software-development-company-in-punjab$', views.dev, name='dev'),
    url(r'^outdoor-advertising-company-punjab$', views.out, name='out'),
    url(r'^branding-company-in-punjab$', views.brand, name='brand'),
    url(r'^content-writing-service-in-punjab$', views.content, name='content'),
    url(r'^logo-designing-company-punjab$', views.logo, name='logo'),
    url(r'^video-editing-services-punjab$', views.video, name='video'),
    url(r'^webp$', views.webp, name='webp'),
    url(r'^digip$', views.digip, name='digip'),
    url(r'^add$', views.add, name='add'),
    url(r'^client$', views.client, name='client'),
    url(r'^why$', views.why, name='why'),
    url(r'^career$', views.career, name='career'),
    url(r'^book', views.book, name='book')
]
