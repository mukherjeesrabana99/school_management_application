from django.shortcuts import render, redirect
from .models import EventCategory, Event, EventMember, EventAgenda
from .forms import EventCategoryForm, EventForm, EventMemberForm, EventAgendaForm

# Create your views here.
def category_list(request):
	cats=EventCategory.objects.all()
	context={'cats':cats}
	return render(request, 'events/category_list.html', context)
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
def delete_category(request, id):
	cat= EventCategory.objects.get(id=id)
	cat.delete()
	return redirect('category_list')
def event_list(request):
	events=Event.objects.all()
	context={'events':events}
	return render(request, 'events/event_list.html', context)

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
def view_event(request, id):
	event= Event.objects.get(id=id)
	context={'event':event}
	return render(request, 'events/view_event.html', context)
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
def delete_event(request, id):
	event= Event.objects.get(id=id)
	event.delete()
	return redirect('event_list')
def member_list(request):
	members=EventMember.objects.all()
	context={'members':members}
	return render(request, 'events/member_list.html', context)
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
def view_member(request, id):
	member= EventMember.objects.get(id=id)
	context={'member':member}
	return render(request, 'events/view_member.html', context)
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
def delete_member(request, id):
	member= EventMember.objects.get(id=id)
	member.delete()
	return redirect('member_list')
def agenda_list(request):
	agenda=EventAgenda.objects.all()
	context={'agenda':agenda}
	return render(request, 'events/agenda_list.html', context)
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
def delete_agenda(request, id):
	agenda= EventAgenda.objects.get(id=id)
	agenda.delete()
	return redirect('agenda_list')