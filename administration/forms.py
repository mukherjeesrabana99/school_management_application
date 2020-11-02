from django import forms
from .models import School, Fees
class SchoolForm(forms.ModelForm):
	class Meta:
		model=School
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'slogan':forms.TextInput(attrs={'class':'form-control'}),
		'country':forms.TextInput(attrs={'class':'form-control'}),
		'city':forms.TextInput(attrs={'class':'form-control'})

		}

class FeesForm(forms.ModelForm):
	class Meta:
		model=Fees
		fields='__all__'
		widgets={
		'class':forms.Select(attrs={'class':'form-control'}),
		'amount':forms.TextInput(attrs={'class':'form-control'}),
		'FeeType':forms.Select(attrs={'class':'form-control'}),
		}

	