from django.db import models
from address.models import Country, City
from academics.models import SchoolClass
import random

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=1000)
	blood_group_select=(
		('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('a-', 'A-'),
        ('o-', 'O-'),
        ('b-', 'B-'),
        ('ab-', 'AB-')
		)
	blood_group=models.CharField(max_length=10, choices=blood_group_select)
	gender_select=(
		('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
		)
	gender=models.CharField(max_length=10, choices=gender_select)
	phone_no=models.CharField(max_length=11)
	email=models.EmailField()
	religion_select=(
		('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'),
        ('Islam', 'Islam'),
        ('Others', 'Others')
		)
	religion=models.CharField(max_length=20, choices=religion_select)
	country=models.ForeignKey(Country, on_delete=models.CASCADE)
	city=models.ForeignKey(City, on_delete=models.CASCADE)
	guardian_name=models.CharField(max_length=100)
	guardian_phone=models.CharField(max_length=11)
	guardian_email=models.EmailField()
	reg_no=models.IntegerField(unique=True, default=random.randint(000000, 999999))
	class_name=models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name='students')
	status=models.BooleanField(default=False)
	paid=models.BooleanField(default=False)
	present=models.BooleanField(default=False)
	def __str__(self):
		return str(self.name)


