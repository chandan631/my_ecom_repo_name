from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product, Cart, Order
from django.contrib.auth.decorators import login_required



@login_required(login_url='/account/signin/')
def add_to_cart(request):
    if request.method == "POST":
        # print('daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        product_id = int(request.POST.get("product_id"))
        product = get_object_or_404(Product, id=product_id)

        # Check if product is already in cart
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

        if not created:
            cart_item.quantity += 1  # If already exists, increase quantity
            cart_item.save()
            message = "Items added with existing items"
        else:
            message = "Items added successfully"

        # Redirect back to the same product page with a success message

        message = "Product added successfully"  # Example message
        url = reverse("product_detail", kwargs={"product_id": product_id}) + f"?message={message}"
        return redirect(url)

    return render(request, "product_detail.html")

@login_required(login_url='/account/signin/')
def cart_page(request, user_id):
    # print('User ID:', user_id)

    # Fetch the user
    user = User.objects.get(id=user_id)
    # print('User:', user)

    # Fetch all cart items for the user
    cart_items = Cart.objects.filter(user_id=user_id)
    # print('Cart Items:', cart_items)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    return render(request, "cart_page.html", {
        'user': user,
        'cart_items': cart_items
    })

@login_required(login_url='/account/signin/')
def order_placed_page(request):
    product_id = int(request.POST.get("product_id"))
    quantity = int(request.POST.get("quantity"))
    user = request.user
    product = Product.objects.get(id=product_id)
    # print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj',user)
    order = Order.objects.create(
            product = product,
            quantity = quantity,
            user = user )
    # print('dddddddddddddddddddddddddd')
    # print(order.id)
    # print(order)
    # print(order.product)

    return render(request, "order_success_page.html", {
        'order': order })

@login_required(login_url='/account/signin/')
def order_history_page(request, user_id):
    # print('hiiiiiiiiiii User ID:', user_id)

    # Fetch the user
    user = User.objects.get(id=user_id)
    # print('byyyyyyyyyy User:', user)

    orders = Order.objects.filter(user_id=user_id)
    # print('hyyyyy orders'  , orders)
    return render(request, "order_history_page.html" , {'orders' : orders , 'user' : user} )









