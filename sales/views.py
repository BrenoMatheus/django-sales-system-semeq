from django.shortcuts import render

def create_sale(request):
    return render(request, 'sales/create_sale.html')

def checkout(request):
    return render(request, "checkout.html")