from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Интернет-Магазин Электроники'
    }
    return render(request, 'catalog/index.html', context)


class ProductDetailView(DetailView):
    model = Product


class CategoryListView(ListView):
    model = Category
    extra_context = {'title': 'Категории товаров'}


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(product_category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk']: category_item.pk
        context_data['title'] = f'Все товары категории: {category_item.category_name}'

        return context_data
