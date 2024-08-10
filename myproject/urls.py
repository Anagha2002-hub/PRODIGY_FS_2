from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Includes URLs from the accounts app
    path('employees/', include('employees.urls')),  # Example for another app
    path('', include('accounts.urls')),  # Includes root URL from accounts app

]
