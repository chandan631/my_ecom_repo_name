
from django.urls import path
from . import views


urlpatterns = [
    path('signin/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout_user'),

]




