# Generated by Django 5.0.2 on 2024-02-26 10:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=256, unique=True, verbose_name='Слаг категории')),
                ('image', models.ImageField(upload_to='category_images', verbose_name='Картинка категории')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_category', to='products.category', verbose_name='Родительская категория')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Название продукта')),
                ('slug', models.SlugField(max_length=256, verbose_name='Слаг продукта')),
                ('image_large', models.ImageField(upload_to='product_images/large/', verbose_name='Картинка товара в высоком разрешении')),
                ('image_medium', models.ImageField(upload_to='product_images/medium', verbose_name='Картинка товара в среднем разрешении')),
                ('image_low', models.ImageField(upload_to='product_images/low', verbose_name='Картинка товара в низком разрешении')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена продукта')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.category', verbose_name='Категория товара')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1, verbose_name='Количество продукта в корзине')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='products.product', verbose_name='Продукт')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
