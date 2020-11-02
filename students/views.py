from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentForm

# Create your views here.
#admin can view student list
def student_list(request):
	students=Student.objects.all().filter(status=True)
	paginator = Paginator(students, 5)
	page_number = request.GET.get('page')
	page_obj=paginator.get_page(page_number)
	context={'students':page_obj}
	return render(request, 'students/student_list.html', context)
#admin can add student
def create_student(request):
	form=StudentForm()
	if request.method=='POST':
		form=StudentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('student_list')
	else:
		context={'form':form}
		return render(request, 'students/create_student.html', context)
#admin can view student ptofile
def student_profile(request, id):
	student=Student.objects.get(id=id)
	context={'student':student}
	return render(request, 'students/student_profile.html', context)
#admin can edit student
def edit_student(request, id):
	student=Student.objects.get(id=id)
	form=StudentForm(instance=student)
	if request.method=='POST':
		form=StudentForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
			return redirect('student_list')
	else:
		context={'form':form}
		return render(request, 'students/edit_student.html', context)
#Admin can delete student
def delete_student(request, id):
	student=Student.objects.get(id=id)
	student.delete()
	return redirect('student_list')
#admin can view unapproved student list
def unapproved_student_list(request):
	students=Student.objects.all().filter(status=False)
	context={'students':students}
	return render(request, 'students/unapproved_student_list.html', context)
#admin can approve an unapproved student
def approve_student(request, id):
	student=Student.objects.get(id=id)
	student.status=True
	student.save()
	return redirect('unapproved_student_list')
#admin can cancel the student without approving him
def cancel_student(request,id):
	student=Student.objects.get(id=id)
	student.delete()
	return redirect('unapproved_student_list')