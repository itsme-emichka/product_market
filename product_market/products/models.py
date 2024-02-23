from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=256,
        unique=True,
    )
    slug = models.SlugField(
        'Слаг категории',
        max_length=256,
        unique=True,
    )
    image = models.ImageField(
        'Картинка категории',
        upload_to='category_images',
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительская категория',
        related_name='child_category',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    @property
    def is_parent(self) -> bool:
        return not bool(self.parent)

    class Meta:
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(
        'Название продукта',
        max_length=512,
    )
    slug = models.SlugField(
        'Слаг продукта',
        max_length=256,
    )
    sub_category = models.ForeignKey(
        Category,
        verbose_name='Категория товара',
        related_name='product',
        on_delete=models.CASCADE,
    )
    image_large = models.ImageField(
        'Картинка товара в высоком разрешении',
        upload_to='product_images/large/',
    )
    image_medium = models.ImageField(
        'Картинка товара в среднем разрешении',
        upload_to='product_images/medium',
    )
    image_low = models.ImageField(
        'Картинка товара в низком разрешении',
        upload_to='product_images/low',
    )
    price = models.DecimalField(
        'Цена продукта',
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('name',)


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Покупатель',
        related_name='cart',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        related_name='cart',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f'{self.user.username} — {self.product.name}'

    class Meta:
        ordering = ('user',)
