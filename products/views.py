from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product


def product_list(request):
    search = request.GET.get("q")

    if search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()

    return render(request, "products/product_list.html", {
        "products": products,
        "search": search or ""
    })
