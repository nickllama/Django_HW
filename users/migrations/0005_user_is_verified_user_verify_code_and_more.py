# Generated by Django 4.2 on 2024-02-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_is_verified_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Верификация'),
        ),
        migrations.AddField(
            model_name='user',
            name='verify_code',
            field=models.CharField(default='2786', max_length=4, verbose_name='Код вeрификации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
