from django.db import models
from address.models import Country, City
from students.models import Student
from academics.models import RegisteredClass, Subject, SchoolClass, Subject
# Create your models here.
class School(models.Model):
	name=models.CharField(max_length=100)
	slogan=models.CharField(max_length=100)
	country=models.ForeignKey(Country, on_delete=models.CASCADE)
	current=models.BooleanField(default=False)
	city=models.ForeignKey(City, on_delete=models.CASCADE)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)


class Fees(models.Model):
	class_name=models.ForeignKey(SchoolClass, on_delete=models.CASCADE, null=True, blank=True)
	fee_type_select=(
		('Admission Fee', 'Admission Fee'),
		('Monthly', 'Monthly'),
		('Yearly', 'Yearly'),

		)
	fee_type=models.CharField(max_length=40, choices=fee_type_select)
	amount=models.CharField(max_length=100)
class Attendance(models.Model):
	date=models.DateField()
	student=models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
	subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
	attendance=models.CharField(max_length=100)