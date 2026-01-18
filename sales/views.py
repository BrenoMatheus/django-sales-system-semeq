from django.shortcuts import render, redirect

def create_sale(request):
    return render(request, 'sales/create_sale.html')

def checkout(request):
    if request.method == "POST":
        # 1. Captura dados do endereço
        # 2. Cria Sale
        # 3. Cria SaleItem
        # 4. Limpa carrinho

        return redirect("order_success")

    return render(request, "checkout.html")

def order_success(request):
    return render(request, "order_success.html")

def order_success(request):
    return render(request, "order_success.html")
