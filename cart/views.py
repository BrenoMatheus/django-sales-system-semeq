from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/cart_detail.html", {"cart": cart})

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    qty = int(request.POST.get("qty", 1))
    override = request.POST.get("override") == "1"

    cart.add(product=product, qty=qty, override=override)

    return redirect("cart_detail")

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)
    return redirect("cart_detail")

def buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = Cart(request)
    qty = int(request.POST.get("qty", 1))

    cart.add(product, qty=qty)

    return redirect("checkout")
