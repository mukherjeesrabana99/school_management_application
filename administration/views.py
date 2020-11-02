from django.shortcuts import render, redirect
from academics.models import Session, SchoolClass, Section, Subject, Shift, RegisteredClass
from .models import School, Fees
from faculty.models import Faculty
from students.models import Student
from notice.models import Notice
from .forms import SchoolForm, FeesForm
from events.models import Event, EventMember
from students.models import Student
from online_tests.models import Exam, ExamMember
# Create your views here.
#Admin can view class count, shift count, section count, current session,schoolname, subject count,
#faculty count, student count, event count, notice count, exam counts

def index(request):
	class_count=SchoolClass.objects.all().count()
	section_count=Section.objects.all().count()
	shift_count=Shift.objects.all().count()
	subject_count=Subject.objects.all().count()
	regcl_count=RegisteredClass.objects.all().count()		
	session=Session.objects.get(current=True)
	notices=Notice.objects.all().order_by('-id')
	notice_count=notices.count()
	faculty=Faculty.objects.all().filter(status=True)
	faculty_count= faculty.count()
	students=Student.objects.all().filter(status=True)
	student_count=students.count()
	event_count=Event.objects.all().count()
	member_count=EventMember.objects.all().count()
	school=School.objects.get(current=True)
	scheduled_exam_count=Exam.objects.all().filter(status="Scheduled").count()
	completed_exam_count=Exam.objects.all().filter(status="Completed").count()
	ongoing_exam_count=Exam.objects.all().filter(status="Ongoing").count()

	context={'session':session, 'notices':notices, 'notice_count':notice_count,   'school':school, 
	'faculty_count':faculty_count, 'student_count':student_count, 'class_count':class_count,
	'shift_count':shift_count, 'subject_count':subject_count, 'section_count':section_count,
	'regcl_count':regcl_count, 'event_count':event_count, 'member_count':member_count,
	'scheduled_exam_count':scheduled_exam_count, 'completed_exam_count':completed_exam_count ,
	 'ongoing_exam_count':ongoing_exam_count}
	return render(request, 'administration/index.html', context)
#Crendering fees page, to view and construct  fees structure
def fees_page(request):
	form=FeesForm()
	if request.method=='POST':
		form=FeesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('fees_page')
	else:
		classes=SchoolClass.objects.all()
		fees=Fees.objects.all()
		context={'form':form, 'classes':classes, 'fees':fees }
		return render(request, 'administration/fees.html', context)
	
#view fee payment status of each student classwisw
def fee_detail(request, cl):
	students=Student.objects.all().filter(class_name=cl)
	context={'students':students}
	return render(request, 'administration/fee_detail.html', context)
from django.shortcuts import render


