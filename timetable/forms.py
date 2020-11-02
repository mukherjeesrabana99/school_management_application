from django import forms
from .models import Timetable
class TableForm(forms.ModelForm):
	class Meta:
		model=Timetable
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'class':forms.Select(attrs={'class':'form-control'}),
		'day1':forms.Select(attrs={'class':'form-control'}),
		'day2':forms.Select(attrs={'class':'form-control'}),
		'day3':forms.Select(attrs={'class':'form-control'}),
		'day4':forms.Select(attrs={'class':'form-control'}),
		'day5':forms.Select(attrs={'class':'form-control'}),
		'ssubjec1':forms.Select(attrs={'class':'form-control'}),
		'subject2':forms.Select(attrs={'class':'form-control'}),
		}