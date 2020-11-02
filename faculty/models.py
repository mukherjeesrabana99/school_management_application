from django.db import models
from address.models import Country, City
import random

# Create your models here.
class Faculty(models.Model):
	name=models.CharField(max_length=100, default="")
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
	blood_group=models.CharField(max_length=10, choices=blood_group_select, default="")
	gender_select=(
		('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
		)
	gender=models.CharField(max_length=10, choices=gender_select,default="" )
	phone_no=models.CharField(max_length=11, default="")
	email=models.EmailField(default="")
	religion_select=(
		('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'),
        ('Islam', 'Islam'),
        ('Others', 'Others')
		)
	religion=models.CharField(max_length=20, choices=religion_select, default="")
	country=models.ForeignKey(Country, on_delete=models.CASCADE, default="")
	city=models.ForeignKey(City, on_delete=models.CASCADE, default="")
	reg_no=models.IntegerField(unique=True, default=random.randint(000000, 999999))
	institute_name=models.CharField(max_length=100, default="")
	passing_exam=models.CharField(max_length=100, default="")
	subject_of_interest=models.CharField(max_length=100, default="")
	status=models.BooleanField(default=False)
	salary_paid=models.BooleanField(default=False)
