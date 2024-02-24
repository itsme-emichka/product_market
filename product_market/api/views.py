from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from api.services import get_all_objects
from api.utils import get_category_parent_and_children


class ProductViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):
    queryset = get_all_objects(Product)
    serializer_class = ProductSerializer


class CategoryViewSet(ListModelMixin,
                      RetrieveModelMixin,
                      GenericViewSet):
    serializer_class = CategorySerializer

    @property
    def category_parent_and_children(self) -> list:
        return get_category_parent_and_children(get_all_objects(Category))

    def get_queryset(self):
        return self.category_parent_and_children[0]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context[
            'category_parents_children'] = self.category_parent_and_children[1]
        return context
