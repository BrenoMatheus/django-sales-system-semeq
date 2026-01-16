# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

def product_list(request):
    search = request.GET.get("search", "")

    products = Product.objects.select_related("category").prefetch_related("suppliers")

    if search:
        products = products.filter(name__icontains=search)

    # Paginação
    paginator = Paginator(products, 6)  # 6 produtos por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "products/product_list.html", {
        "page_obj": page_obj,
        "search": search,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, "products/product_detail.html", {
        "product": product
    })
