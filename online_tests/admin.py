from django.contrib import admin
from .models import ExamType, Exam, ExamAgenda, ExamMember
# Register your models here.
admin.site.register(ExamType)
admin.site.register(Exam)
admin.site.register(ExamMember)
admin.site.register(ExamAgenda)