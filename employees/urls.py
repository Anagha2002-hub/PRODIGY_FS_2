# employees/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns for employees here
    path('', views.employee_home, name='employee_home'),
]
