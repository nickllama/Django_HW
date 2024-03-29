from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    IndexListView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='IndexListView'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', ProductListView.as_view(), name='category_products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('<int:pk>/product/', ProductDeleteView.as_view(), name='delete_product'),
]
