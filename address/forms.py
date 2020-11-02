from django import forms
from .models import Country, City
class CountryForm(forms.ModelForm):
	class Meta:
		model=Country
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'})
		}


class CityForm(forms.ModelForm):
	class Meta:
		model=City
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'country':forms.Select(attrs={'class':'form-control'})
		}