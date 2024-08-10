from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This should correspond to the home view
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]
