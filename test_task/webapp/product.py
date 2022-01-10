from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, 
    CreateView, 
    DetailView,
    DeleteView
    )
from django.db.models import Q
from django.utils.http import urlencode
from webapp.models import Product, Card

from webapp.forms import SearchForm, ProductForm

class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ('product_name',)
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProductListView, self).get(request, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(product_name__icontains=self.search_data) |
                Q(price__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context

class ProductView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product


class ProductCreateView(CreateView):
    template_name = 'product/product_create.html' 
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save()
        return redirect('webapp:product_detail', pk=product.pk)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('webapp:product_list')

