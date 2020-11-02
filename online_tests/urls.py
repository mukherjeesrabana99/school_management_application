from django.urls import path
from . import views
urlpatterns=[
#Exam type urls
path('types/', views.type_list, name='type_list'),
path('create_type/', views.create_type, name='create_type'),
path('edit_type/<int:id>/', views.edit_type, name='edit_type'),
path('delete_type/<int:id>/', views.delete_type, name='delete_type'),

#Exam urls
path('', views.exam_list, name='exam_list'),
path('create_exam/', views.create_exam, name='create_exam'),
path('edit_exam/<int:id>/', views.edit_exam, name='exam'),
path('delete_exam/<int:id>/', views.delete_exam, name='delete_exam'),

#Exam agenda urls
path('agenda/', views.agenda_list, name='agenda_list'),
path('create_agenda/', views.create_agenda, name='create_agenda'),
path('view_agenda/<int:id>/', views.view_agenda, name='view_agenda'),
path('edit_agenda/<int:id>/', views.edit_agenda, name='edit_agenda'),
path('delete_agenda/<int:id>/', views.delete_agenda, name='delete_agenda'),
#Exam member urls
path('examinees/', views.member_list, name='member_list'),
path('create_member/', views.create_member, name='create_member'),
path('view_member/<int:id>/', views.view_member, name='view_member'),
path('edit_member/<int:id>/', views.edit_member, name='edit_member'),
path('delete_member/<int:id>/', views.delete_member, name='delete_member'),

]