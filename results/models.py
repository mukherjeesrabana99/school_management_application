from django.db import models
from students.models import Student
from academics.models import Subject
# Create your models here.
class Result(models.Model):
	student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
	subject=models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
	test_score=models.IntegerField()
	exam_score=models.IntegerField()
	def total(self):
		return self.test_score + self.exam_score
	