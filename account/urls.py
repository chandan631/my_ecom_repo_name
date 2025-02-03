# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signin/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),

]




