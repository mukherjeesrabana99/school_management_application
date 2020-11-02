from django import forms
from .models import EventCategory, Event, EventMember, EventAgenda
class EventCategoryForm(forms.ModelForm):
	class Meta:
		model=EventCategory
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'code':forms.TextInput(attrs={'class':'form-control'}),
		'status':forms.Select(attrs={'class':'form-control'}),
		}

	
class EventForm(forms.ModelForm):
	class Meta:
		model=Event
		fields='__all__'
		widgets={
		'category':forms.Select(attrs={'class':'form-control'}),
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'description':forms.TextInput(attrs={'class':'form-control'}),
		'start_date':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
		'end_date':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
		'status':forms.Select(attrs={'class':'form-control'}),
				}
class EventMemberForm(forms.ModelForm):
	class Meta:
		model=EventMember
		fields='__all__'
		widgets={
		'event':forms.Select(attrs={'class':'form-control'}),
		'members':forms.Select(attrs={'class':'form-control'}),
		'attnedance':forms.Select(attrs={'class':'form-control'}),
		}
class EventAgendaForm(forms.ModelForm):
	class Meta:
		model=EventAgenda
		fields='__all__'
		widgets={
		'event':forms.Select(attrs={'class':'form-control'}),
		'session_name':forms.TextInput(attrs={'class':'form-control'}),
		'start_time':forms.TextInput(attrs={'class':'form-control', 'type':'time'}),
		'end_time':forms.TextInput(attrs={'class':'form-control', 'type':'time'}),
		'speaker':forms.TextInput(attrs={'class':'form-control'}),
		}