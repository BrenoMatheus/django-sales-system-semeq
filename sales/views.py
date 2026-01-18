from datetime import date
from decimal import Decimal
from django.shortcuts import render, redirect
from .models import Sale, SaleItem
from products.models import Product
from customers.models import Customer
from django.utils import timezone
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

def create_sale(request):
    return render(request, 'sales/create_sale.html')

@login_required
def checkout(request):
    cart = Cart(request)
    customer = request.user.customer


    if not cart:
        return redirect("product_list")  # ou página de produtos

    if request.method == "POST":

        # 1. Criar a venda
        sale = Sale.objects.create(
            #customer=request.user.customer,
            customer=customer,
            sale_date=timezone.now().date(),

            cep=request.POST.get("cep"),
            street=request.POST.get("rua"),
            neighborhood=request.POST.get("bairro"),
            city=request.POST.get("cidade"),
            state=request.POST.get("estado"),
        )

        # 2. Criar os itens da venda
        for item in cart:
            product = Product.objects.get(id=item["id"])
            print(item)
            SaleItem.objects.create(
                sale=sale,
                product=product,
                #product=item["product"],
                quantity=item["qty"],
                unit_price=item["price"],
            )

        # 3. Limpar carrinho
        cart.clear()

        # 4. Redirecionar para sucesso
        return redirect("order_success")

    return render(request, "checkout.html")

@login_required
def sales_history(request):
    sales = Sale.objects.filter(
        customer__user=request.user
    ).order_by("-created_at")

    return render(request, "sales/history.html", {
        "sales": sales
    })


def order_success(request):
    return render(request, "order_success.html")

def order_success(request):
    return render(request, "order_success.html")
