from django.urls import path
from . import views
urlpatterns=[
path('', views.timetable_list, name='timetable_list'),
path('create_timetable/', views.create_timetable, name='create_timetable'),
path('edit_timetable/<int:id>/', views.edit_timetable, name='edit_timetable'),
path('delete_timetable/<int:id>/', views.delete_timetable, name='delete_timetable'),

]