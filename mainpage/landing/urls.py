from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Landing Page
    path('login', views.login, name='login'), # Login page
    path('register', views.register, name='register') # Register Page
]
