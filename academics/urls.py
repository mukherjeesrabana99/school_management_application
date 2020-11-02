from django.urls import path
from . import views
urlpatterns=[
# Class URLS
path('classes/', views.create_class, name='create_class'),
path('edit_class/<int:cl_id>/', views.edit_class, name='edit_class'),
path('delete_class/<int:cl_id>/', views.delete_class, name='delete_class'),

# SECTION URLS
path('sections/', views.create_section, name='create_section'),
path('edit_section/<int:sec_id>/', views.edit_section, name='edit_section'),
path('delete_section/<int:sec_id>/', views.delete_section, name='delete_section'),

# SEESION URLS
path('sessions/', views.create_session, name='create_session'),
path('edit_session/<int:ses_id>/', views.edit_session, name='edit_session'),
path('delete_session/<int:ses_id>/', views.delete_session, name='delete_session'),
# SUBJECT URLS
path('subjects/', views.create_subject, name='create_subject'),
path('edit_subject/<int:sub_id>/', views.edit_subject, name='edit_subject'),
path('delete_subject/<int:sub_id>/', views.delete_subject, name='delete_subject'),

# SHIFT URLS
path('shifts/', views.create_shift, name='create_shift'),
path('edit_shift/<int:shift_id>/', views.edit_shift, name='edit_shift'),
path('delete_shift/<int:shift_id>/', views.delete_shift, name='delete_shift'),

# REGISTERED CLASS URLS
path('registered_class/', views.create_registeredclass, name='create_registeredclass'),
path('edit_regclass/<int:cl_id>/', views.edit_regclass, name='edit_regclass'),
path('delete_regclass/<int:cl_id>/', views.delete_regclass, name='delete_regclass'),

]