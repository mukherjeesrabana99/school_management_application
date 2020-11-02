from django.db import models
from academics.models import Session
from students.models import Student

# Create your models here.

class ExamType(models.Model):
	name=models.CharField(max_length=100)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)

class Exam(models.Model):
	name=models.CharField(max_length=100)
	exam_type=models.ForeignKey(ExamType, on_delete=models.CASCADE, null=True)
	start_date=models.DateField()
	end_date=models.DateField()
	status_select=(
		('Scheduled', 'Scheduled'),
		('Ongoing', 'Ongoing'),
		('Completed', 'Completed'),
		)
	status=models.CharField(max_length=100, choices=status_select, default="")
	session=models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)
class ExamAgenda(models.Model):
	exam=models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
	syllabus=models.TextField()
	start_time=models.TimeField()
	end_time=models.TimeField()
	date=models.DateField(auto_now_add=True)
class ExamMember(models.Model):
	exam=models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
	student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
	attendance_select=(
		('Present', 'Present'),
		('Absent', 'Absent'),
		)
	attendance=models.CharField(max_length=100, choices=attendance_select)