from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import FeedbackForm
from .models import Category, Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Интернет-Магазин Электроники'
    }
    return render(request, 'catalog/index.html', context)


# def categories(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Категории товаров'
#     }
#     return render(request, 'catalog/category_list.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {'title': 'Категории товаров'}


# def category_products(request, pk):
#     category_item = Category.objects.get(pk=pk)
#
#     context = {
#         'object_list': Product.objects.filter(product_category_id=pk),
#         'title': f'Все товары категории: {category_item.category_name}'
#     }
#     return render(request, 'catalog/product_list.html', context)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(product_category_id=self.kwargs('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk']: category_item.pk
        context_data['title'] = f'Все товары категории: {category_item.category_name}'

        return context_data


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})


def contacts(request):
    return render(request, 'catalog/contacts.html')


def FeedbackForm(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных формы (например, сохранение в базу данных)
            # Здесь можно добавить логику для обработки отправленной обратной связи

            # После обработки формы, можно, например, перенаправить пользователя
            return render(request, 'thank_you_page.html')
    else:
        form = FeedbackForm()

    return render(request, 'contacts.html', {'form': form})
