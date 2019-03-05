# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib import messages

from .forms import ContactForm, BookForm
from .models import Contact, Book


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'cities/city.html'

    def get_success_url(self):
        return reverse('city:city')

    def form_valid(self, form):
        model = Contact()

        model.name = form.cleaned_data['name']
        model.city = form.cleaned_data['city']
        model.state = form.cleaned_data['state']
        model.comment = form.cleaned_data['comment']
        model.latitude = form.cleaned_data['latitude']
        model.longitude = form.cleaned_data['longitude']
        model.save()
        if form:
            messages.info(self.request, 'Thank you for your message. We will be in touch shortly.')
        else:
            messages.error(self.request, "We couldn't send your message. Please try again later.")
        return super(ContactView, self).form_valid(form)

from django.shortcuts import render

def contacts(request):
    items = Contact.objects.all()
    return render(request, 'cities/cities.html', locals())

class BookView(FormView):
    form_class = BookForm
    template_name = 'cities/book.html'

    def get_success_url(self):
        return reverse('city:city')

    def form_valid(self, form):
        model = Book()

        model.name = form.cleaned_data['name']
        model.phone = form.cleaned_data['phone']
        model.price = form.cleaned_data['price']
        model.comment = form.cleaned_data['comment']
        model.save()
        if form:
            messages.info(self.request, 'Thank you for your message. We will be in touch shortly.')
        else:
            messages.error(self.request, "We couldn't send your message. Please try again later.")
        return super(ContactView, self).form_valid(form)