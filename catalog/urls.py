from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ProductListView, product_detail, index

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', ProductListView.as_view(), name='category_products'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
