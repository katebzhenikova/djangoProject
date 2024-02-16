from django.shortcuts import render
from django.views.generic import DetailView

from mainapp.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'SHOP online'
    }
    return render(request, 'main/index.html', context)


def products(request):
    context = {
        'product_list': Product.objects.all(),
        'title': 'SHOP online - Products'
    }
    return render(request, 'main/products.html', context)


def product_page(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'product_page': Product.objects.filter(product_category_id=pk),
        'product': product_item,
        'title': 'SHOP online - Products'

    }
    return render(request, 'main/product_page.html', context)


# def products(request, pk):
#     if pk == 0:
#         product_item = Category.objects.all()
#     else:
#         product_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(product_category_id=pk),
#         'products': product_item
#     }
#     return render(request, 'main/products.html', context)



