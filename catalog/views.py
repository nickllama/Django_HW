from django.conf import settings
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductForm, VersionForm
from .models import Category, Product, Version


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Интернет-Магазин Электроники'

        for product in context['object_list']:
            product.active_version = product.version_set.filter(is_active=True).first()

        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        product = self.object  # Получаем объект продукта из представления

        product.active_version = product.version_set.filter(is_active=True).first()

        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {'title': 'Категории товаров'}


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': "Каталог продуктов",
        'current_user': settings.AUTH_USER_MODEL,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(product_category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk']: category_item.pk
        context_data['title'] = f'Все товары категории: {category_item.category_name}'

        for product in context_data['object_list']:
            product.active_version = product.version_set.filter(is_active=True).first()

        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:IndexListView')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:IndexListView')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:IndexListView')
