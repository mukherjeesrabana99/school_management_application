from django.urls import path
from . import views
urlpatterns=[
path('', views.result_list, name='result_list'),
path('create_result/', views.create_result, name='create_result'),
path('edit_result/<int:id>/', views.edit_result, name='edit_result'),
path('delete_result/<int:id>/', views.delete_result, name='delete_result'),
]