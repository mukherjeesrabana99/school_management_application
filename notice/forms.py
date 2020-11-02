from django import forms
from .models import Notice



class NoticeForm(forms.ModelForm):
	class Meta:
		model=Notice
		fields='__all__'
		widgets={
		'topic':forms.TextInput(attrs={'class':'form-control'}),
		'body':forms.TextInput(attrs={'class':'form-control'}),
		}