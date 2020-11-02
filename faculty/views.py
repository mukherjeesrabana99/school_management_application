from django.shortcuts import render, redirect
from .models import Faculty
from .forms import FacultyForm
# Create your views here.
def faculty_list(request):
	faculties=Faculty.objects.all().filter(status=True)
	context={'faculties':faculties}
	return render(request, 'faculty/faculty_list.html', context)
def create_faculty(request):
	form=FacultyForm()
	if request.method=='POST':
		form=FacultyForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('faculty_list')
	else:
		context={'form':form}
		return render(request, 'faculty/create_faculty.html', context)
def faculty_detail(request, id):
	faculty=Faculty.objects.get(id=id)
	context={'faculty': faculty}
	return render(request, 'faculty/faculty_detail.html', context)
def edit_faculty(request, id):
	faculty=Faculty.objects.get(id=id)
	form=FacultyForm(instance=faculty)
	if request.method=='POST':
		form=FacultyForm(request.POST, instance=faculty)
		if form.is_valid():
			form.save()
			return redirect('faculty_list')
	else:
		context={'form':form}
		return render(request, 'faculty/edit_faculty.html', context)

def delete_faculty(request, id):
	faculty=Faculty.objects.get(id=id)
	faculty.delete()
	return redirect('faculty_list')