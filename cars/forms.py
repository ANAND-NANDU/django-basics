from django import forms

class carForm(forms.Form):
	name=forms.CharField(label="name",max_length=100)
	company=forms.CharField(label="company",max_length=100)
