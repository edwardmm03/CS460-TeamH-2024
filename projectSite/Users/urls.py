from django.urls import path
from . import views

urlpatterns = [
    path('Users/', views.Users, name='Users'),
]