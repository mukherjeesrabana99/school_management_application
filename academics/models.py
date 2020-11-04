from django.db import models
from faculty.models import Faculty
# Create your models here.
class SchoolClass(models.Model):
	name=models.CharField(max_length=10)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)
class Section(models.Model):
	name=models.CharField(max_length=10)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)
class Shift(models.Model):
	name=models.CharField(max_length=100)
	start_time=models.TimeField()
	end_time=models.TimeField()
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)
class Session(models.Model):
	session_start=models.DateField()
	session_end=models.DateField()
	name=models.CharField(max_length=10, default='')
	current=models.BooleanField(default=False)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)
class Subject(models.Model):
	name=models.CharField(max_length=100)
	faculty=models.ForeignKey(Faculty, on_delete=models.CASCADE)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)

class RegisteredClass(models.Model):
	scl_class=models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
	section=models.ForeignKey(Section, on_delete=models.CASCADE)
	session=models.ForeignKey(Session, on_delete=models.CASCADE)
	shift=models.ForeignKey(Shift, on_delete=models.CASCADE, null=True, default="")
	subjects=models.ForeignKey(Subject, on_delete=models.CASCADE)
	name=models. CharField(max_length=100, default="")
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)




