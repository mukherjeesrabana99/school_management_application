from django import forms
from .models import SchoolClass, Section, Session, Shift, RegisteredClass, Subject
class SchoolClassForm(forms.ModelForm):
	class Meta:
		model=SchoolClass
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'})
		}
class SectionForm(forms.ModelForm):
	class Meta:
		model=Section
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'})
		}
class SessionForm(forms.ModelForm):
	class Meta:
		model=Session
		fields='__all__'
		widgets={
		'StartYear':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
		'EndYear':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
		'name':forms.TextInput(attrs={'class':'form-control'})
		}
class ShiftForm(forms.ModelForm):
	class Meta:
		model=Shift
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'start':forms.Select(attrs={'class':'form-control', 'type':'time'}),
		'end':forms.Select(attrs={'class':'form-control', 'type':'time'})
		}
class SubjectForm(forms.ModelForm):
	class Meta:
		model=Subject
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'faculty':forms.Select(attrs={'class':'form-control'})
		}
class RegisteredClassForm(forms.ModelForm):
	class Meta:
		model=RegisteredClass
		fields='__all__'
		widgets={
		'scl_class':forms.Select(attrs={'class':'form-control'}),
		'section':forms.Select(attrs={'class':'form-control'}),
		'session':forms.Select(attrs={'class':'form-control'}),
		'subject':forms.Select(attrs={'class':'form-control'}),
		'shift':forms.Select(attrs={'class':'form-control'}),
		'name':forms.TextInput(attrs={'class':'form-control'})
		}