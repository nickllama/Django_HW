from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import categories, category_products, product_detail, index

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
