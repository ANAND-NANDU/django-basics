from django import forms
from .models import cars

class carForm(forms.Form):
	name=forms.CharField(label="name",max_length=100)
	company=forms.CharField(label="company",max_length=100)

class carModelForm(forms.ModelForm):
	class Meta:
		model=cars
		fields = "__all__"	
	
