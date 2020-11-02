from django.shortcuts import render, redirect
from .models import Notice
from .forms import NoticeForm
# Create your views here.
#Admin can view notice
def notice_list(request):
	notices=Notice.objects.all()
	context={'notices':notices}
	return render(request, 'notice/notice_list.html', context)
#Admin can create notice
def create_notice(request):
	form=NoticeForm()
	if request.method=='POST':
		form=NoticeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('notice_list')
	else:
		
		context={'form':form}
		return render(request, 'notice/create_notice.html', context)
#Admin can edit notice
def edit_notice(request, id):
	notice=Notice.objects.get(id=id)
	form=NoticeForm(instance=notice)
	if request.method=='POST':
		form=NoticeForm(request.POST, instance=notice)
		if form.is_valid():
			form.save()
			return redirect('notice_list')
	else:
		context={'form':form}
		return render(request, 'notice/edit_notice.html', context)
#Admin can delete notice
def delete_notice(request, id):
	notice=Notice.objects.get(id=id)
	notice.delete()
	return redirect('notice_list')