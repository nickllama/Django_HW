from django.shortcuts import render, get_object_or_404
from .forms import FeedbackForm
from .models import Category, Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Интернет-Магазин Электроники'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/categories.html', context)


def category_products(request, category_id):
    category_item = Category.objects.get(pk=category_id)

    context = {
        'object_list': Product.objects.filter(product_category=category_item),
        'title': f'Все товары категории: {category_item.category_name}'
    }
    return render(request, 'catalog/Products.html', context)


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
