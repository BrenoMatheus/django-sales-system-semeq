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

def create_sale(request):
    return render(request, 'sales/create_sale.html')

@login_required
def checkout(request):
    cart = Cart(request)

    # Garante que o usuário tenha customer
    if not hasattr(request.user, "customer"):
        messages.error(request, "Usuário sem perfil de cliente.")
        return redirect("product_list")

    customer = request.user.customer

    # Se carrinho vazio
    if not cart or len(cart) == 0:
        messages.warning(request, "Seu carrinho está vazio.")
        return redirect("product_list")

    if request.method == "POST":

        # Captura dados
        cep = request.POST.get("cep")
        rua = request.POST.get("rua")
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        estado = request.POST.get("estado")

        # Validação simples (obrigatórios)
        if not all([cep, rua, bairro, cidade, estado]):
            messages.error(request, "Preencha todos os campos do endereço.")
            return render(request, "checkout.html")

        # 1. Criar venda
        sale = Sale.objects.create(
            customer=customer,
            sale_date=timezone.now().date(),
            cep=cep,
            street=rua,
            neighborhood=bairro,
            city=cidade,
            state=estado,
        )

        # 2. Criar itens da venda
        for item in cart:
            product = Product.objects.get(id=item["id"])

            SaleItem.objects.create(
                sale=sale,
                product=product,
                quantity=item["qty"],
                unit_price=item["price"],
            )

        # 3. Limpa carrinho
        cart.clear()

        messages.success(request, "Compra finalizada com sucesso!")
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
