from django.contrib import admin
from .models import SchoolClass, Section, Session, Shift, RegisteredClass, Subject
# Register your models here.
admin.site.register(SchoolClass)
admin.site.register(Section)
admin.site.register(Session)
admin.site.register(Shift)

admin.site.register(Subject)
admin.site.register(RegisteredClass)
