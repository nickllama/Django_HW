# Generated by Django 5.0 on 2024-02-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(default='blog_images/default.png', upload_to='blog_images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(verbose_name='содержимое'),
        ),
    ]