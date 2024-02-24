from django.db.models import Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import Http404

from products.models import Cart, Product
from users.models import User as User_model


User: User_model = get_user_model()


def get_all_objects(model: Model) -> QuerySet:
    return model.objects.all()


def add_product_to_cart(
        user: User_model,
        product_id: int,
        amount: int = 1) -> Cart:
    if not isinstance(amount, int):
        amount = 1
    product = get_object_or_404(Product, id=product_id)
    try:
        cart_position: Cart = get_object_or_404(
            Cart,
            user=user,
            product=product
        )
        cart_position.amount += amount
        cart_position.save()
    except Http404:
        cart_position = Cart.objects.create(
            user=user,
            product=product,
            amount=amount,
        )
    finally:
        return cart_position


def delete_product_from_cart(user: User_model, product_id: int) -> None:
    get_object_or_404(Cart, user=user, product_id=product_id).delete()
