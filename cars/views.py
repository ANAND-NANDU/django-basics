from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.

def index(request):

	cars = models.cars.objects.all()
	if(cars.exists() == False):
		a=models.cars(name="msutang",company="ford").save()
		print("creating mock data")
	else:
		print("data exists")
	
	return render(request,"cars/index.html")

