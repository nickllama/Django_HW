from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ProductListView, ProductDetailView, index

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', ProductListView.as_view(), name='category_products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
