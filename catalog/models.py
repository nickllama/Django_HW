from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    product_description = models.TextField(max_length=100, verbose_name='Описание', **NULLABLE)
    product_image = models.ImageField(upload_to='product_images/', verbose_name='Изображение (превью)', **NULLABLE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за штуку')
    product_date_of_creation = models.DateField(auto_now_add=True)
    product_date_of_modification = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.product_name} - {self.product_price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('product_name',)
