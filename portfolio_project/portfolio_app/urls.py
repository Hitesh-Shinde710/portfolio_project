from django.urls import path
from . import views  # We'll create views.py content later

urlpatterns = [
    path('', views.home, name='home'),  # Placeholder for now
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]