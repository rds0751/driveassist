# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Contact, Book

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'comment', 'latitude', 'longitude')
# Register your models here.
admin.site.register(Contact, ContactAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'price', 'comment')
# Register your models here.
admin.site.register(Book, BookAdmin)
