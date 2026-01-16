# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    search = request.GET.get("search", "")

    products = Product.objects.select_related("category").prefetch_related("suppliers")

    if search:
        products = products.filter(name__icontains=search)

    return render(request, "products/product_list.html", {
        "products": products,
        "search": search,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, "products/product_detail.html", {
        "product": product
    })
