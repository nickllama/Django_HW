# Generated by Django 4.2 on 2024-02-12 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Верификация'),
        ),
    ]
