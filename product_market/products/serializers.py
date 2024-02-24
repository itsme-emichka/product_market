from typing import Any

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from products.models import Product, Category


class CategorySerializer(ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'image',
            'sub_categories',
        )

    def get_sub_categories(self, obj: Category) -> list[dict[str, Any]]:
        if not obj.is_parent:
            return []
        category_parents_children: dict = self.context.get(
            'category_parents_children')
        return CategorySerializer(
            instance=category_parents_children.get(obj.id, []),
            many=True,
            context=category_parents_children,
        ).data


class ProductSerializer(ModelSerializer):
    sub_category = serializers.StringRelatedField(read_only=True)
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'category',
            'sub_category',
            'image_large',
            'image_medium',
            'image_low',
            'price',
        )

    def get_category(self, obj: Product) -> str:
        parent = obj.sub_category.parent
        if parent:
            return parent.name
        return None
