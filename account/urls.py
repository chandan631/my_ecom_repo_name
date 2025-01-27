# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),

    # path('logout/', views.user_logout, name='logout'),  # If you need a logout functionality
]
