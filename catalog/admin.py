from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price', 'product_category']
    list_filter = ['product_category__category_name']
    search_fields = ['product_name', 'product_description']