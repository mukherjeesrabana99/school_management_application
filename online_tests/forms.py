from django import forms
from .models import ExamType, Exam, ExamAgenda, ExamMember
class ExamTypeForm(forms.ModelForm):
	class Meta:
		model=ExamType
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		}
class ExamForm(forms.ModelForm):
	class Meta:
		model=Exam
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'exam_type':forms.Select(attrs={'class':'form-control'}),
		'session':forms.Select(attrs={'class':'form-control'}),
		'start_date':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
		'end_date':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
		'status':forms.TextInput(attrs={'class':'form-control'}),
		}
class ExamAgendaForm(forms.ModelForm):
	class Meta:
		model=ExamAgenda
		fields='__all__'
		widgets={
		'exam':forms.Select(attrs={'class':'form-control'}),
		'syllabus':forms.TextInput(attrs={'class':'form-control'}),
		'start_time':forms.TextInput(attrs={'class':'form-control', 'type':'time'}),
		'end_time':forms.TextInput(attrs={'class':'form-control', 'type':'time'}),
		}
class ExamMemberForm(forms.ModelForm):
	class Meta:
		model=ExamMember
		fields='__all__'
		widgets={
		'exam':forms.Select(attrs={'class':'form-control'}),
		'student':forms.Select(attrs={'class':'form-control'}),
		'attendance':forms.Select(attrs={'class':'form-control'}),
		}