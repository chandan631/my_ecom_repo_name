# my_shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),

]
