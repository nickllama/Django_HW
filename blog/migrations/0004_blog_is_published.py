# Generated by Django 5.0 on 2024-02-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_created_at_alter_blog_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Признак публикации'),
        ),
    ]
