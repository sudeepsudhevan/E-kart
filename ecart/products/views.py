from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    return render(request, "index.html")


def list_products(request):
    """_summary_
    return: product list page

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    page = 1
    if request.GET:
        page = request.GET.get("page", 1)  # get the page number from the request

    product_list = Product.objects.order_by("-priority")
    product_paginator = Paginator(product_list, 2)
    product_list = product_paginator.get_page(page)
    context = {"products": product_list}
    return render(request, "products.html", context)


def detail_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
