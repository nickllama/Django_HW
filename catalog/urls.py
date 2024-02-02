from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import index, categories, category_products

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:id>/catalog', category_products, name='category_products'),
]