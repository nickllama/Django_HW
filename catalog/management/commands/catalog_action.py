from django.core.management.base import BaseCommand
from django.db import connection
from catalog.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Очистка таблицы Product
        Product.objects.all().delete()

        # Очистка таблицы Category
        Category.objects.all().delete()

        # Сброс автоинкремента для поля `pk` в таблице Category
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        # Сброс автоинкремента для поля `pk` в таблице Product
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")

        # Создание категорий
        categories = [
            {'category_name': 'Холодильники', 'category_description': 'Бытовые холодильники'},
            {'category_name': 'Телевизоры', 'category_description': 'Телевизоры для дома'},
            {'category_name': 'Микроволновки', 'category_description': 'Микроволновки для кухни'},
            {'category_name': 'Стиральные машины', 'category_description': 'Бытовые стиральные машины'},
            {'category_name': 'Ноутбуки', 'category_description': 'Ноутбуки и компьютеры'},
        ]

        # Сохранение категорий в базе данных
        Category.objects.bulk_create([Category(**category) for category in categories])

        # Получение объектов Category
        category_objects = {category.category_name: category for category in Category.objects.all()}

        # Создание товаров
        products = [
            {'product_name': 'Samsung RS3000', 'product_description': 'Двухкамерный холодильник', 'product_price': 79999, 'product_category': 'Холодильники'},
            {'product_name': 'LG OLED CX', 'product_description': '4K OLED телевизор', 'product_price': 69999, 'product_category': 'Телевизоры'},
            {'product_name': 'Bosch HMT72G450', 'product_description': 'Микроволновая печь с грилем', 'product_price': 12999, 'product_category': 'Микроволновки'},
            {'product_name': 'Bosch Serie 4', 'product_description': 'Стиральная машина', 'product_price': 39999, 'product_category': 'Стиральные машины'},
            {'product_name': 'Dell XPS 13', 'product_description': 'Ноутбук с процессором Intel Core i7', 'product_price': 89999, 'product_category': 'Ноутбуки'},
        ]

        # Сохранение товаров в базе данных
        products_for_create = []
        for product_item in products:
            # Получаем объект Category по имени
            category_name = product_item.pop('product_category')
            product_item['product_category'] = category_objects.get(category_name)

            products_for_create.append(Product(**product_item))

        # Сохраняем товары в базе данных
        Product.objects.bulk_create(products_for_create)

        print(products_for_create, categories)

        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены в базу данных.'))
