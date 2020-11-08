from django.shortcuts import render, redirect
from .models import Timetable
from .forms import TableForm
# Create your views here.
#Admin can view timetable list of all classes
def timetable_list(request):
	tables=Timetable.objects.all()
	context={'tables':tables}
	return render(request, 'timetable/table_list.html', context)
#Admin can create Time table
def create_timetable(request):
	form=TableForm()
	if request.method=='POST':
		form=TableForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('timetable_list')
	else:
		context={'form':form}
		return render(request, 'timetable/create_timetable.html', context)
#Admin can edit timetable
def edit_timetable(request, id):
	table=Timetable.objects.get(id=id)
	form=TableForm(instance=table)
	if request.method=='POST':
		form=TableForm(request.POST, instance=table)
		if form.is_valid():
			form.save()
			return redirect('timetable_list')
	else:
		context={'form':form}
		return render(request, 'timetable/edit_timetable.html', context)
#Admin can delete timetable
def delete_timetable(request, id):
	table=Timetable.objects.get(id=id)
	table.delete()
	return redirect('timetable_list')