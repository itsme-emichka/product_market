# Generated by Django 5.0.2 on 2024-02-23 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='sub_category',
        ),
    ]
