from django.shortcuts import render
from django.http import HttpResponse

from . import models
from .forms import carForm
# Create your views here.

def index(request):

	cars = models.cars.objects.all()
	if(cars.exists() == False):
		a=models.cars(name="msutang",company="ford").save()
		print("creating mock data")
	else:
		print("data exists")
		print(cars)
	
	return render(request,"cars/index.html")
	
def new_car(request):
	if (request.method == 'POST'):
		form = carForm(request.POST)
		if(form.is_valid()):
			print (form.cleaned_data)
			a=models.cars(name=form.cleaned_data.get("name"),company=form.cleaned_data.get("company")).save()
		else:
			print("invalid")
			
	else:
		print("free load")

	return render(request,"cars/new_car.html")
	
	

	

