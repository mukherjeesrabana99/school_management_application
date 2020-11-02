from django.urls import path
from . import views
urlpatterns=[

path('', views.index, name='index'),
path('fees_page/', views.fees_page, name='fees_page'),
path('fee_detail/<int:cl>/', views.fee_detail, name='fee_detail'),

]