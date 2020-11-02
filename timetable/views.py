from django.shortcuts import render, redirect
from .models import Timetable
from .forms import TableForm
# Create your views here.
def timetable_list(request):
	tables=Timetable.objects.all()
	context={'tables':tables}
	return render(request, 'timetable/table_list.html', context)
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
def edit_timetable(request, id):
	table=Timetable.objects.get(id=id)
	form=TableForm(instance=table)
	if request.metho=='POST':
		form=TableForm(request.POST, instance=table)
		if form.is_valid():
			form.save()
			return redirect('timetable_list')
	else:
		context={'form':form}
		return render(request, 'timetable/edit_timetable.html', context)
def delete_timetable(request, id):
	table=Timetable.objects.get(id=id)
	table.delete()
	return redirect('timetable_list')