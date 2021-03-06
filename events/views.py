from django.shortcuts import render, redirect
from .models import EventCategory, Event, EventMember, EventAgenda
from .forms import EventCategoryForm, EventForm, EventMemberForm, EventAgendaForm

# Create your views here.
#Admin can view event category list
def category_list(request):
	cats=EventCategory.objects.all()
	context={'cats':cats}
	return render(request, 'events/category_list.html', context)
#Admin can create event category
def create_category(request):
	form=EventCategoryForm()
	if request.method=='POST':
		form=EventCategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('category_list')
	else:
		context={'form':form}
		return render(request, 'events/create_category.html', context)
#Admin can edit event category 
def edit_category(request, id):
	cat= EventCategory.objects.get(id=id)
	form=EventCategoryForm(instance=cat)
	if request.method=='POST':
		form=EventCategoryForm(request.POST, instance=cat)
		if form.is_valid():
			form.save()
			return redirect('category_list')
	else:
		context={'form':form}
		return render(request, 'events/edit_category.html', context)
#Admin can delete event category 
def delete_category(request, id):
	cat= EventCategory.objects.get(id=id)
	cat.delete()
	return redirect('category_list')
#Admin can view event  list
def event_list(request):
	events=Event.objects.all()
	context={'events':events}
	return render(request, 'events/event_list.html', context)
#Admin can create event 
def create_event(request):
	form=EventForm()
	if request.method=='POST':
		form=EventForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('event_list')
	else:
		context={'form':form}
		return render(request, 'events/create_event.html', context)
#Admin can view event details
def view_event(request, id):
	event= Event.objects.get(id=id)
	context={'event':event}
	return render(request, 'events/view_event.html', context)
#Admin can edit event
def edit_event(request, id):
	event= Event.objects.get(id=id)
	form=EventForm(instance=event)
	if request.method=='POST':
		form=EventForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
			return redirect('event_list')
	else:
		context={'form':form}
		return render(request, 'events/edit_event.html', context)
#Admin can delete event
def delete_event(request, id):
	event= Event.objects.get(id=id)
	event.delete()
	return redirect('event_list')
#Admin can  view event member list
def member_list(request):
	members=EventMember.objects.all()
	context={'members':members}
	return render(request, 'events/member_list.html', context)
# Admin can create member
def create_member(request):
	form=EventMemberForm()
	if request.method=='POST':
		form=EventMemberForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('member_list')
	else:
		context={'form':form}
		return render(request, 'events/create_member.html', context)
# Admin can view event member details
def view_member(request, id):
	member= EventMember.objects.get(id=id)
	context={'member':member}
	return render(request, 'events/view_member.html', context)
# Admin can edit member
def edit_member(request, id):
	member= EventMember.objects.get(id=id)
	form=EventMemberForm(instance=member)
	if request.method=='POST':
		form=EventMemberForm(request.POST, instance=member)
		if form.is_valid():
			form.save()
			return redirect('member_list')
	else:
		context={'form':form}
		return render(request, 'events/edit_member.html', context)
# Admin can delete member
def delete_member(request, id):
	member= EventMember.objects.get(id=id)
	member.delete()
	return redirect('member_list')
# Admin can view event agenda list
def agenda_list(request):
	agenda=EventAgenda.objects.all()
	context={'agenda':agenda}
	return render(request, 'events/agenda_list.html', context)
#Admin can create agenda
def create_agenda(request):
	form=EventAgendaForm()
	if request.method=='POST':
		form=EventAgendaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('agenda_list')
	else:
		context={'form':form}
		return render(request, 'events/create_agenda.html', context)
#Admin can edit agenda
def edit_agenda(request, id):
	agenda= EventAgenda.objects.get(id=id)
	form=EventAgendaForm(instance=agenda)
	if request.method=='POST':
		form=EventAgendaForm(request.POST, instance=agenda)
		if form.is_valid():
			form.save()
			return redirect('agenda_list')
	else:
		context={'form':form}
		return render(request, 'events/edit_agenda.html', context)
#Admin can delete Agenda
def delete_agenda(request, id):
	agenda= EventAgenda.objects.get(id=id)
	agenda.delete()
	return redirect('agenda_list')