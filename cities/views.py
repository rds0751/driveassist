# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib import messages

from django.shortcuts import render

from .forms import ContactForm
from .models import Contact


def book(request):
    print("r")
    context={}
    if request.method == 'POST':
        way0 =request.POST['way0']
        way1=request.POST['way1']
        print(way0)
        print(way1)
        context={
        'way0': way0,
        'way1': way1,
        }

    return render(request, 'core/book.html',context)

def contacts(request):
    items = Contact.objects.all()
    return render(request, 'cities/cities.html', locals())