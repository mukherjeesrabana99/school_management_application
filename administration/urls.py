from django.urls import path
from . import views
urlpatterns=[

path('', views.index, name='index'),
path('fees_page/', views.fees_page, name='fees_page'),
path('fee_detail/<int:cl>/', views.fee_detail, name='fee_detail'),


#ATTENDANCE URLS
path('attendance/', views.attendance_list, name='attendance_list'),
path('create_attendance/', views.create_attendance, name='create_attendance'),
path('edit_attendance/<int:id>/', views.edit_attendance, name='edit_attendance'),

]