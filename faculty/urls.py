from django.urls import path
from . import views
urlpatterns=[
path('', views.faculty_list, name='faculty_list'),
path('create_faculty/', views.create_faculty, name='create_faculty'),
path('faculty_detail/<int:id>/', views.faculty_detail, name='faculty_detail'),
path('edit_faculty/<int:id>/', views.edit_faculty, name='edit_faculty'),
path('delete_faculty/<int:id>/', views.delete_faculty, name='delete_faculty'),


]