from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    body = models.TextField(verbose_name='Cодержимое')
    photo = models.ImageField(upload_to='blog_images/', default='blog_images/default.png', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации', editable=False)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    # def save(self, *args, **kwargs):
    #     # Генерация slug на основе заголовка, если он не указан
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} {self.created_at}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
