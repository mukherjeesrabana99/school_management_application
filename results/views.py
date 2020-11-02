from django.shortcuts import render
from .models import ExamType, Exam, ExamAgenda, ExamMember
from .forms import ExamTypeForm, ExamForm, ExamAgendaForm, ExamMemberForm 
# Create your views here.
#Admin can view types of exams in a list
def type_list(request):
	types=ExamType.objects.all()
	context={'types':types}
	return render(request, 'exams/type_list.html', context)
#Admin can create exam type
def create_type(request):
	form=ExamTypeForm()
	if request.method=='POST':
		form=ExamTypeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('type_list')
	else:
		context={'form':form}
		return render(request, 'exams/create_type.html', context)
#Admin can edit exam type
def edit_type(request, id):
	exam_type=ExamType.objects.get(id=id)
	form=ExamTypeForm(instance=exam_type)
	if request.method=='POST':
		form=ExamTypeForm(request.POST, instance=exam_type)
		if form.is_valid():
			form.save()
			return redirect('type_list')
	else:
		context={'form':form}
		return render(request, 'exams/edit_type.html', context)
#Admin can delete exam type
def delete_type(request, id):
	exam_type=ExamType.objects.get(id=id)
	exam_type.delete()
	return redirect('type_list')
#Admin can view exam list
def exam_list(request):
	exams=Exam.objects.all()
	context={'exams':exams}
	return render(request, 'exams/exam_list.html', context)
#Admin can create exam
def create_exam(request):
	form=ExamForm()
	if request.method=='POST':
		form=ExamForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('exam_list')
	else:
		context={'form':form}
		return render(request, 'exams/create_exam.html', context)
#Admin can edit exam
def edit_exam(request, id):
	exam=Exam.objects.get(id=id)
	form=ExamForm(instance=exam)
	if request.method=='POST':
		form=ExamForm(request.POST, instance=exam)
		if form.is_valid():
			form.save()
			return redirect('exam_list')
	else:
		context={'form':form}
		return render(request, 'exams/edit_exam.html', context)
#Admin can delete exam
def delete_exam(request, id):
	exam=Exam.objects.get(id=id)
	exam.delete()
	return redirect('exam_list')
#Admin can view exam agenda list
def agenda_list(request):
	agenda=ExamAgenda.objects.all()
	context={'agenda':agenda}
	return render(request, 'exams/agenda_list.html', context)
#Admin can create event agend
def create_agenda(request):
	form=ExamAgendaForm()
	if request.method=='POST':
		form=ExamAgendaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('agenda_list')
	else:
		context={'form':form}
		return render(request, 'exams/create_agenda.html', context)
#admin can view agenda detail
def view_agenda(request, id):
	agenda=ExamAgenda.objects.get(id=id)
	context={'agenda':agenda}
	return render(request, 'exams/view_agenda.html', context)
#Admin can edit agenda
def edit_agenda(request, id):
	agenda=ExamAgenda.objects.get(id=id)
	form=ExamAgendaForm(instance=agenda)
	if request.method=='POST':
		form=ExamAgendaForm(request.POST, instance=agenda)
		if form.is_valid():
			form.save()
			return redirect('agenda_list')
	else:
		context={'form':form}
		return render(request, 'exams/edit_agenda.html', context)
#Admin can delete agenda
def delete_agenda(request, id):
	agenda=ExamAgenda.objects.get(id=id)
	agenda.delete()
	return redirect('agenda_list')
#Admin can view examinees/exam-member list
def member_list(request):
	members=ExamMember.objects.all()
	context={'members':members}
	return render(request, 'exams/member_list.html', context)
#Admin can add examinee
def create_member(request):
	form=ExamMemberForm()
	if request.method=='POST':
		form=ExamMemberForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('member_list')
	else:
		context={'form':form}
		return render(request, 'exams/create_member.html', context)
#Admin can view examinee details
def view_member(request, id):
	member=ExamMember.objects.get(id=id)
	context={'member':member}
	return render(request, 'exams/view_member.html', context)
#Admin can edit examinee
def edit_member(request, id):
	member=ExamMember.objects.get(id=id)
	form=ExamMemberForm(instance=member)
	if request.method=='POST':
		form=ExamMemberForm(request.POST, instance=member)
		if form.is_valid():
			form.save()
			return redirect('member_list')
	else:
		context={'form':form}
		return render(request, 'exams/edit_member.html', context)
#Admin can delete examinee
def delete_member(request, id):
	member=ExamMember.objects.get(id=id)
	member.delete()
	return redirect('member_list')