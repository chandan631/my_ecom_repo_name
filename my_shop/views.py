from django.shortcuts import get_object_or_404, render, redirect
from my_shop.models import Category , Product
from django.core.paginator import Paginator
# Create your views here.


def redirect_to_shop(request):

    return redirect("/shop/product/")


def product(request,category_id=None):
    categorys = Category.objects.all()
    products = Product.objects.all()

    if category_id is None:
        products = products
    else :
        products = products.filter(category_id = category_id)

    paginator = Paginator(products,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'product.html',{'categorys':categorys, 'page_obj':page_obj })


def product_detail(request, product_id):
    # print("gttttttttttteeffffffffffffffffffffffffffffffff")
    product = get_object_or_404(Product, id=product_id)  # Only filter by product_id
    return render(request, 'product_detail.html', {'product': product})












