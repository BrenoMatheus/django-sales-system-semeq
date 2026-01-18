from datetime import date
from decimal import Decimal
from django.shortcuts import render, redirect
from .models import Sale, SaleItem
from products.models import Product
from customers.models import Customer
from django.utils import timezone
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CheckoutForm

def create_sale(request):
    return render(request, 'sales/create_sale.html')

@login_required
def checkout(request):
    cart = Cart(request)

    # ✅ forma correta de validar carrinho vazio
    if not cart.cart:
        messages.warning(request, "Seu carrinho está vazio.")
        return redirect("product_list")

    # ✅ evita crash se usuário não tiver customer
    try:
        customer = request.user.customer
    except:
        messages.error(request, "Seu usuário não possui perfil de cliente.")
        return redirect("/")

    if request.method == "POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():
            sale = Sale.objects.create(
                customer=customer,
                sale_date=timezone.now().date(),
                cep=form.cleaned_data["cep"],
                street=form.cleaned_data["rua"],
                neighborhood=form.cleaned_data["bairro"],
                city=form.cleaned_data["cidade"],
                state=form.cleaned_data["estado"],
            )

            for item in cart:
                product = Product.objects.get(id=item["id"])
                SaleItem.objects.create(
                    sale=sale,
                    product=product,
                    quantity=item["qty"],
                    unit_price=item["price"],
                )

            cart.clear()
            messages.success(request, "Compra realizada com sucesso!")
            return redirect("order_success")

        messages.error(request, "Preencha corretamente os dados do endereço.")

    form = CheckoutForm()
    return render(request, "checkout.html", {"form": form})


    return render(request, "checkout.html", {"form": form})


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
