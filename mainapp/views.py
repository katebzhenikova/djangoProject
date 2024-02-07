from django.shortcuts import render

from mainapp.models import Category, Product


def index(request):
    category_id_ind = request.GET.get('category')
    category_list = Category.objects.all()
    context = {
        'object_list': category_list
    }
    return render(request, 'main/index.html', context)


def products(request):
    category_id = request.GET.get('category')
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
        'category_id': category_id
    }
    return render(request, 'main/products.html', context)


# def products(request):
#     category_id = request.GET.get('category')
#     products = Product.objects.all()
#     if category_id:
#         products = products.filter(product_category_id=category_id)
#     return render(request, 'products.html', {'products': products})






# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#     return render(request, 'main/index.html')
