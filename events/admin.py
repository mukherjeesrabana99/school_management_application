from django.contrib import admin
from .models import EventCategory, Event, EventMember, EventAgenda
# Register your models here.
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(EventAgenda)
admin.site.register(EventMember)