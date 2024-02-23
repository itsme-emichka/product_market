# Generated by Django 5.0.2 on 2024-02-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена продукта'),
            preserve_default=False,
        ),
    ]