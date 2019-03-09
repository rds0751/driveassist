from django.db import models

class Contact(models.Model):
	name = models.CharField(
        max_length=500,)
	phone = models.CharField(max_length=12, null=True, blank=True)
	latitude = models.CharField(max_length=1000, null=True)
	longitude = models.CharField(max_length=1000, null=True)
	