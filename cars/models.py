from django.db import models

# Create your models here.

class cars(models.Model):
	name = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
