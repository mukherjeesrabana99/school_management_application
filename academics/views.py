from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import SchoolClass, Section, Session, Shift,  RegisteredClass, Subject
from.forms import SchoolClassForm, SectionForm, SessionForm,  ShiftForm, RegisteredClassForm, SubjectForm
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
# Create your views here.
# Admin can create class
def create_class(request):
	class_form=SchoolClassForm()
	if request.method=='POST':
		form=SchoolClassForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_class')
	else:
		classes=SchoolClass.objects.all()
		context={'form':class_form, "classes":classes}
		return render(request, 'academics/class.html', context)
#Admin edit class
def edit_class(request, cl_id):
	cl=SchoolClass.objects.get(id=cl_id)
	form=SchoolClassForm(instance=cl)
	if request.method=='POST':
		form=SchoolClassForm(request.POST, instance=cl)
		if form.is_valid():
			form.save()
			return redirect('create_class')
	else:
		context={'form':form}
		return render(request, 'academics/edit_class.html', context)
#admin can delete class
def delete_class(request, cl_id):
	cl=SchoolClass.objects.get(id=cl_id)
	cl.delete()
	return redirect('create_class')
# Admin can create section
def create_section(request):
	section_form=SectionForm()
	if request.method=='POST':
		form=SectionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_section')
	else:
		sections=Section.objects.all()
		context={'form':section_form, 'sections':sections}
		return render(request, 'academics/section.html', context)
#Admin can edit section
def edit_section(request, sec_id):
	sec=Section.objects.get(id=sec_id)
	form=SectionForm(instance=sec)
	if request.method=='POST':
		form=SectionForm(request.POST, instance=sec)
		if form.is_valid():
			form.save()
			return redirect('create_section')
	else:
		context={'form':form}
		return render(request, 'academics/edit_section.html', context)
#Admin can delete section
def delete_section(request, sec_id):
	sec=Section.objects.get(id=sec_id)
	sec.delete()
	return redirect('create_section')
# Admin can create session
def create_session(request):
	form=SessionForm()
	if request.method=='POST':
		form=SessionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_session')
	else:
		sessions=Session.objects.all()
		context={'form':form, 'sessions':sessions}
		return render(request, 'academics/session.html', context)
#Admin can edit session
def edit_session(request, ses_id):
	ses=Session.objects.get(id=ses_id)
	form=SessionForm(instance=ses)
	if request.method=='POST':
		form=SessionForm(request.POST, instance=ses)
		if form.is_valid():
			form.save()
			return redirect('create_session')
	else:
		context={'form':form}
		return render(request, 'academics/edit_session.html', context)
#admin can delete session
def delete_session(request, ses_id):
	ses=Session.objects.get(id=ses_id)
	ses.delete()
	return redirect('create_session')
# Admin create shift
def create_shift(request):
	form=ShiftForm()
	if request.method=='POST':
		form=ShiftForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_shift')
	else:
		shifts=Shift.objects.all()
		context={'form':form, 'shifts':shifts}
		return render(request, 'academics/shift.html', context)
#admin can edit shift
def edit_shift(request, shift_id):
	shift=Shift.objects.get(id=shift_id)
	form=ShiftForm(instance=shift)
	if request.method=='POST':
		form=ShiftForm(request.POST, instance=shift)
		if form.is_valid():
			form.save()
			return redirect('create_shift')
	else:
		context={'form':form}
		return render(request, 'academics/edit_shift.html', context)
#Admin can delete shift
def delete_shift(request, shift_id):
	shift=Shift.objects.get(id=shift_id)
	shift.delete()
	return redirect('create_shift')
# Create registered class using  Registered Class Model
def create_registeredclass(request):
	form=RegisteredClassForm()
	if request.method=='POST':
		form=RegisteredClassForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_registeredclass')
	else:
		classes=RegisteredClass.objects.all()
		context={'form':form, 'classes':classes}
		return render(request, 'academics/reg_class.html', context)
# Applying CRUD to Subject Model
def create_subject(request):
	form=SubjectForm()
	if request.method=='POST':
		form=SubjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_subject')
	else:
		subjects=Subject.objects.all()
		context={'form':form, 'subjects':subjects}
		return render(request, 'academics/subject.html', context)
def edit_subject(request, sub_id):
	sub=Subject.objects.get(id=sub_id)
	form=SubjectForm(instance=sub)
	if request.method=='POST':
		form=SubjectForm(request.POST, instance=sub)
		if form.is_valid():
			form.save()
			return redirect('create_subject')
	else:
		context={'form':form}
		return render(request, 'academics/edit_subject.html', context)
def delete_subject(request, sub_id):
	sub=Subject.objects.get(id=sub_id)
	sub.delete()
	return redirect('create_subject')
# Edit registered class using  Registered Class Model
def edit_regclass(request, cl_id):
	cl=RegisteredClass.objects.get(id=cl_id)
	form=RegisteredClassForm(instance=cl)
	if request.method=='POST':
		form=RegisteredClassForm(request.POST, instance=cl)
		if form.is_valid():
			form.save()
			return redirect('create_registeredclass')
	else:
		context={'form':form}
		return render(request, 'academics/edit_regcl.html', context)
#Delete registered class using  Registered Class Model
def delete_regclass(request, cl_id):
	cl=RegisteredClass.objects.get(id=cl_id)
	cl.delete()
	return redirect('create_registeredclass')
