from django.db import models
from students.models import Student

# Create your models here.
class EventCategory(models.Model):
	name=models.CharField(max_length=1000)
	code=models.CharField(max_length=10)
	status_select=(
		('Active', 'Active'),
		('Disabled', 'Disabled'),
		)
	staus=models.CharField(max_length=100, choices=status_select)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)
class Event(models.Model):
	category=models.ForeignKey(EventCategory, on_delete=models.CASCADE, null=True)
	name=models.CharField(max_length=100)
	description=models.TextField()
	start_date=models.DateField()
	end_date=models.DateField()
	status_select=(
		('Active', 'Active'),
		('Disabled', 'Disabled'),

		)
	staus=models.CharField(max_length=100, choices=status_select)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)
class EventMember(models.Model):
	event=models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
	members=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
	attendance_select=(
		('Present', 'Present'),
		('Absent', 'Absent'),
		)
	attendance=models.CharField(max_length=100, choices=attendance_select)

class EventAgenda(models.Model):
	event=models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
	session_name=models.CharField(max_length=100)
	start_time=models.TimeField()
	end_time=models.TimeField()
	speaker_name=models.CharField(max_length=100)
