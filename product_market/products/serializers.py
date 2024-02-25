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
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'category',
            'sub_category',
            'images',
            'price',
        )

    def get_category(self, obj: Product) -> str:
        parent = obj.sub_category.parent
        if parent:
            return parent.name
        return None

    def get_images(self, obj: Product) -> list[str]:
        # Более удобный вариант выдачи изображений.
        # return {
        #     'image_large': obj.image_large.url,
        #     'image_medium': obj.image_medium.url,
        #     'image_low': obj.image_low.url,
        # }
        return [obj.image_large.url, obj.image_medium.url, obj.image_low.url]


class ProductCartSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            **ProductSerializer(instance.product).data,
            'amount': instance.amount,
            'final_price': instance.product.price * instance.amount
        }
