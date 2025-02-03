from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/', views.add_to_cart, name="add_to_cart"),
    path('cart-page/<int:user_id>/', views.cart_page, name="cart_page"),
    path('order-placed-page/', views.order_placed_page, name="order_placed_page"),
    path('order-history-page/<int:user_id>/', views.order_history_page, name="order_history_page"),

]
