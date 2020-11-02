from django.db import models
from academics.models import RegisteredClass, Subject
# Create your models here.
class Timetable(models.Model):
	name=models.CharField(max_length=100)
	class_name=models.ForeignKey(RegisteredClass, on_delete=models.CASCADE, null=True)
	day_select=(
		('Monday', 'Monday'),
		('Tuesday', 'Tuesday'),
		('Wednesday', 'Wednesday'),
		('Thursday', 'Thursday'),
		('Friday', 'Friday'),
		)
	day1=models.CharField(max_length=30, choices=day_select)
	day2=models.CharField(max_length=30, choices=day_select)
	day3=models.CharField(max_length=30, choices=day_select)
	day4=models.CharField(max_length=30, choices=day_select)
	day5=models.CharField(max_length=30, choices=day_select)
	sub1=models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="sub1", null=True)
	sub2=models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="sub2", null=True)
	sub1_time=models.TimeField()
	sub2_time=models.TimeField()
	break_time=models.TimeField()
	scl_over_time=models.TimeField()
	