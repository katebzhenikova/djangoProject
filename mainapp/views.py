from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from mainapp.models import Category, Product, Blog

class ProductListView(ListView):
    model = Product
    template_name = 'main/products.html'


# def products(request):
#     context = {
#         'product_list': Product.objects.all(),
#         'title': 'SHOP online - Products'
#     }
#     return render(request, 'main/products.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_page.html'


# def product_page(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'product_page': Product.objects.filter(product_category_id=pk),
#         'product': product_item,
#         'title': 'SHOP online - Products'
#
#     }
#     return render(request, 'main/product_page.html', context)

class BlogCreateView(CreateView):
    model = Blog
    fields = ('blog_title', 'description', 'blog_image')
    success_url = reverse_lazy('mainapp:blog_list')
    template_name = 'main/blog_form.html'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.blog_title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    fields = ('blog_title', 'description', 'blog_image')
    success_url = reverse_lazy('mainapp:blog_list')
    template_name = 'main/blog_list.html'
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(blog_is_published=True)
        return queryset



class BlogDetailView(DetailView):
    model = Blog
    fields = ('blog_title', 'description', 'blog_image')
    success_url = reverse_lazy('mainapp:blog_detail')
    template_name = 'main/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('blog_title', 'description', 'blog_image')
    success_url = reverse_lazy('mainapp:blog_list')
    template_name = 'main/blog_form.html'


class BlogDeleteView(DeleteView):
    model = Blog
    fields = ('blog_title', 'description', 'blog_image')
    success_url = reverse_lazy('mainapp:blog_list')
    template_name = 'main/blog_confirm_delete.html'








# def index(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'SHOP online'
#     }
#     return render(request, 'main/index.html', context)

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



