# -*- coding: utf-8 -*-

from smtplib import SMTPException

from django import forms
from django.core.mail import EmailMessage
from .models import Contact
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.HiddenInput())
    latitude = forms.CharField(
        required=True,
        widget=forms.HiddenInput())
    longitude = forms.CharField(
        required=True,
        widget=forms.HiddenInput())

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'latitude', 'longitude',)
