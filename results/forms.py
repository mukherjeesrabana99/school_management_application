from django import forms
from .models import Result
class ResultForm(forms.ModelForm):
	class Meta:
		model=Result
		fields='__all__'
		widhets={
		'student':forms.Select(attrs={'class':'form-control'}),
		'subject':forms.Select(attrs={'class':'form-control'}),
		'TestScore':forms.NumberInput(attrs={'class':'form-control'}),
		'ExamScore':forms.NumberInput(attrs={'class':'form-control'}),
		}