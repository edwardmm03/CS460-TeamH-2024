from django.urls import path
from . import views

urlpatterns = [
    path('Users/', views.Users, name='Users'),
    path('Administrator/', views.Administrator, name = 'Administrator'),
    path('Instructor/', views.Instructor, name = 'Instructor'),
    path('Student/', views.Student, name = 'Student'),
    path('StudentResults/', views.StudentResults, name = 'StudentResults'),
    path('CourseList/', views.CourseList, name = 'CourseList'),
    path('StudentList/', views.StudentList, name = 'StudentList'),
    path('InstructorList/', views.InstructorList, name = 'InstructorList'),
    path('DeptSals/', views.DeptSals, name = 'DeptSals'),
    path('Performance/', views.Performance, name = 'Performance')
]