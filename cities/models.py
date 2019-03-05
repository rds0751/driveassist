from django.db import models

class Contact(models.Model):
	name = models.CharField(
        max_length=500,)
	city = models.CharField(max_length=20,)
	state = models.CharField(
        max_length=100,)
	comment = models.CharField(max_length=1000,)
	longitude = models.CharField(max_length=1000, null=True)
	latitude = models.CharField(max_length=1000, null=True)

class Book(models.Model):
	name = models.CharField(
        max_length=100,)
	phone = models.CharField(max_length=20,)
	price = models.CharField(
        max_length=100,)
	comment = models.CharField(max_length=1000,)