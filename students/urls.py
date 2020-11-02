from django.urls import path
from . import views
urlpatterns=[
path('', views.student_list, name='student_list'),
path('create_student/', views.create_student, name='create_student'),
path('student_profile/<int:id>/', views.student_profile, name='student_profile'),
path('edit_student/<int:id>/', views.edit_student, name='edit_student'),
path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
#Urls for unappproved students
path('unapproved_students/', views.unapproved_student_list, name='unapproved_student_list'),
path('approve_student/<int:id>/', views.approve_student, name='approve_student'),
path('cancel_student/', views.cancel_student, name='cancel_student'),



]