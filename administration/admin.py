from django.contrib import admin
from .models import School, Fees, Attendance
# Register your models here.
admin.site.register(School)
admin.site.register(Fees)
admin.site.register(Attendance)
