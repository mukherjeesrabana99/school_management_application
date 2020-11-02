from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		
		'blood_group':forms.Select(attrs={'class': 'form-control'}),
		
		'gender':forms.Select(attrs={'class': 'form-control'}),
		'phone_number':forms.TextInput(attrs={'class': 'form-control'}),
		'email':forms.TextInput(attrs={'class': 'form-control'}),
		'religion':forms.Select(attrs={'class': 'form-control'}),
		'country':forms.Select(attrs={'class': 'form-control'}),
		'city':forms.Select(attrs={'class': 'form-control'}),
		'GuardianName':forms.TextInput(attrs={'class': 'form-control'}),
		'GuardianPhone':forms.TextInput(attrs={'class': 'form-control'}),
		'GuardianEmail':forms.TextInput(attrs={'class': 'form-control'}),
		'RegistrationNumber':forms.TextInput(attrs={'class': 'form-control'}),
		'Class':forms.Select(attrs={'class': 'form-control'}),

		}