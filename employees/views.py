# employees/views.py
from django.http import HttpResponse

def employee_home(request):
    return HttpResponse("Welcome to the employees page!")
