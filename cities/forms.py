# -*- coding: utf-8 -*-

from smtplib import SMTPException

from django import forms
from django.core.mail import EmailMessage
from .models import Contact, Book


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder': "Name *", 'required': ""}),
    )
    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder': "City *", 'required': ""}),
    )
    state = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder': "State *", 'required': ""}),
    )
    comment = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'type': "text", 'class': "form-control", 'placeholder': "Comment On Uniploe Location *", 'required': ""}),
    )
    latitude = forms.CharField(
        required=True,
        widget=forms.HiddenInput())
    longitude = forms.CharField(
        required=True,
        widget=forms.HiddenInput())

    class Meta:
        model = Contact
        fields = ('name', 'city', 'state', 'comment', 'latitude', 'longitude',)

class BookForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder': "Name of Unipole Location*", 'required': ""}),
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder': "Phone Number*", 'required': ""}),
    )
    price = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder': "Price*", 'required': ""}),
    )
    comment = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'type': "text", 'class': "form-control", 'placeholder': "Any Specific Requirements", 'required': ""}),
    )

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'price', 'comment',)