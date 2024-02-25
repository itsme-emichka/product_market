from django.db.models.query import QuerySet

from products.models import Category


def get_category_parent_and_children(
        categories_queryset: QuerySet
        ) -> list[list[Category], dict[int, list[Category]]]:
    parents = []
    category_parents_children = dict()

    for category in categories_queryset:
        if category.is_parent:
            parents.append(category)
            continue
        children_list: list = category_parents_children.get(
            category.parent_id, [])
        if not children_list:
            category_parents_children[category.parent_id] = [category]
        else:
            children_list.append(category)

    return parents, category_parents_children


def get_total_amount_and_price(cart_queryset: QuerySet) -> list[int]:
    total_amount = 0
    total_price = 0
    for obj in cart_queryset:
        total_amount += obj.amount
        total_price += obj.product.price
    return total_amount, total_price
