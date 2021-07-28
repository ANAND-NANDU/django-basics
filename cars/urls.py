from django.urls import path
from . import views

urlpatterns = [
	
	path('',views.index),
	path('new_car/',views.new_car),
	
	
	]
