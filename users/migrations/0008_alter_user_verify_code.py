# Generated by Django 4.2 on 2024-02-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_verify_email_user_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_code',
            field=models.CharField(default='3873', max_length=4, verbose_name='Код вeрификации'),
        ),
    ]
