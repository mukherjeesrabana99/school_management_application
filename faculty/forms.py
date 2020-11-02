from django import forms
from .models import Faculty
class FacultyForm(forms.ModelForm):
	class Meta:
		model=Faculty
		fields='__all__'
		widgets={
		'name':forms.TextInput(),
		'gender':forms.Select(),
		'religion':forms.Select(),
		'email':forms.TextInput(),
		'phone_no':forms.TextInput(),
		'institute_name':forms.TextInput(),
		'exam_name':forms.TextInput(),
		'reg_no':forms.TextInput(),
		'subject':forms.TextInput(),
		'blood_gro':forms.Select(),
		'country':forms.Select(),
		'city':forms.Select(),

		}