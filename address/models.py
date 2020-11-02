from django.db import models

# Create your models here.
class Country(models.Model):
	name=models.CharField(max_length=30)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)
class City(models.Model):
	name=models.CharField(max_length=30)
	country=models.ForeignKey(Country, on_delete=models.CASCADE)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.name)