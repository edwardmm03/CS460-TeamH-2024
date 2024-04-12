from django.urls import path
from . import views

urlpatterns = [
    path('Users/', views.Users, name='Users'),
    path('Administrator/', views.Administrator, name = 'Administrator'),
    path('Instructor/', views.Instructor, name = 'Instructor'),
    path('Student/', views.Student, name = 'Student'),
    path('StudentResults/', views.StudentResults, name = 'StudentResults')
]