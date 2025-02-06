# my_shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product, name='product'),
    path('product/<int:category_id>/', views.product, name='category_product'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),

]
