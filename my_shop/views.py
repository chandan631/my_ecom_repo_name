from django.shortcuts import get_object_or_404, render, redirect
from my_shop.models import Category , Product
# Create your views here.


def redirect_to_shop(request):

    return redirect("/shop/home/")


def home(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    p = None
    if request.method == 'POST':
        p =  request.POST.get('category_id')
        x = int(p)
        if x == 0 :
            products = products
        else :
            products = products.filter(category_id = x)
    return render(request, 'home.html',{'categorys':categorys, 'products':products })


def product_detail(request, product_id):
    # print("gttttttttttteeffffffffffffffffffffffffffffffff")
    product = get_object_or_404(Product, id=product_id)  # Only filter by product_id
    return render(request, 'productpage.html', {'product': product})












