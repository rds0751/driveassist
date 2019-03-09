# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib import messages

from .forms import ContactForm
from .models import Contact


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'core/book.html'
    success_url = 'book/thankyou/'

    def form_valid(self, form):
        model = Contact()

        model.name = form.cleaned_data['name']
        model.latitude = form.cleaned_data['latitude']
        model.longitude = form.cleaned_data['longitude']
        model.phone = self.request.user.profile.phone
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