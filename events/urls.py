from django.urls import path
from . import views
urlpatterns=[
path('categories/', views.category_list, name='category_list'),
path('create_category/', views.create_category, name='create_category'),
path('edit_category/<int:id>/', views.edit_category, name='edit_category'),
path('delete_category/<int:id>/', views.delete_category, name='delete_category'),
path('', views.event_list, name='event_list'),
path('create_event/', views.create_event, name='create_event'),
path('view_event/<int:id>/', views.view_event, name='view_event'),
path('edit_event/<int:id>/', views.edit_event, name='edit_event'),
path('delete_event/<int:id>/', views.delete_event, name='delete_event'),
path('members/', views.member_list, name='member_list'),
path('create_member/', views.create_member, name='create_member'),
path('view_member/<int:id>/', views.view_member, name='view_member'),
path('edit_member/<int:id>/', views.edit_member, name='edit_member'),
path('delete_member/<int:id>/', views.delete_member, name='delete_member'),
path('agenda/', views.agenda_list, name='agenda_list'),
path('create_agenda/', views.create_agenda, name='create_agenda'),
path('edit_agenda/<int:id>/', views.edit_agenda, name='edit_agenda'),
path('delete_agenda/<int:id>/', views.delete_agenda, name='delete_agenda'),


]