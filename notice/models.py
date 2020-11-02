from django.db import models

# Create your models here.
class Notice(models.Model):
	heading=models.CharField(max_length=100)
	body=models.TextField(max_length=1000)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.heading)
