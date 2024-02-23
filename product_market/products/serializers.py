from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from products.models import Product


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

    def get_category(self, obj) -> str:
        parent = obj.sub_category.parent
        if parent:
            return parent.name
        return None
