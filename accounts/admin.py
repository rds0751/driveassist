# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'phone', 'birth_date')
# Register your models here.
admin.site.register(Profile, ProfileAdmin)