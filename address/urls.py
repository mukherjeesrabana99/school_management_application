from django.urls import path
from . import views
urlpatterns=[
# COUNTRY URLS
path('countries/', views.create_country, name='create_country' ),
path('edit_country/<int:id>/', views.edit_country, name='edit_country'),
path('delete_country/<int:id>/', views.delete_country, name='delete_country'),
# COUNTRY URLS
path('cities/', views.create_city, name='create_city'),
path('edit_city/<int:id>/', views.edit_city, name='edit_city'),
path('delete_city/<int:id>/', views.delete_city, name='delete_city'),
]