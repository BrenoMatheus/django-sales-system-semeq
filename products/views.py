# Create your views here.
from django.shortcuts import render, get_object_or_404
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

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, "products/product_detail.html", {
        "product": product
    })
