from django.shortcuts import render, redirect
from results.models import Result
from results.forms import ResultForm
# Create your views here.
#Admin can view result
def result_list(request):
	results=Result.objects.all()
	context={'results':results}
	return render(request, 'results/result_list.html', context)
#Admin can create result
def create_result(request):
	form=ResultForm()
	if request.method=='POST':
		form=ResultForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('result_list')
	else:
		context={'form':form}
		return render(request, 'results/create_result.html', context)
#Admin can edit result
def edit_result(request, id):
	result=Result.objects.get(id=id)
	form=ResultForm(instance=result)
	if request.method=='POST':
		form=ResultForm(request.POST, instance=result)
		if form.is_valid():
			form.save()
			return redirect('result_list')
	else:
		context={'form':form}
		return render(request, 'results/edit_result.html', context)
#Admin can delete result
def delete_result(request, id):
	result=Result.objects.get(id=id)
	result.delete()
	return redirect('result_list')