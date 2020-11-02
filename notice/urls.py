from django.urls import path
from . import views
urlpatterns=[
path('', views.notice_list, name='notice_list'),
path('create_notice/', views.create_notice, name='create_notice'),
path('edit_notice/<int:id>/', views.edit_notice, name='edit_notice'),
path('delete_notice/<int:id>/', views.delete_notice, name='delete_notice'),
]