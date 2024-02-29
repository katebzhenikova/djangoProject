from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from mainapp.forms import ProductForm, VersionForm
from mainapp.models import Category, Product, Blog, Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('mainapp:products')
    template_name = 'main/product_form.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('mainapp:products')
    template_name = 'main/product_form.html'

    def get_form_class(self):
        return super().get_form_class()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()

        return super().form_valid(form)






class ProductListView(ListView):
    model = Product
    template_name = 'main/products_list.html'



# def products(request):
#     context = {
#         'product_list': Product.objects.all(),
#         'title': 'SHOP online - Products'
#     }
#     return render(request, 'main/products_list.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_page.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('mainapp:products')
    template_name = 'main/products_list.html'


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
        # queryset = queryset.filter(blog_is_published=True)
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
    template_name = 'main/blog_form.html'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.blog_title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mainapp:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    fields = ('blog_title', 'description', 'blog_image')
    success_url = reverse_lazy('mainapp:blog_list')
    template_name = 'main/blog_confirm_delete.html'


def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.blog_is_published:
        blog_item.blog_is_published = False
    else:
        blog_item.blog_is_published = True

    blog_item.save()

    return redirect(reverse('mainapp:blog_list'))










