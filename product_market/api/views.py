from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from products.models import Product
from products.serializers import ProductSerializer
from api.services import get_all_objects


class ProductViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):
    queryset = get_all_objects(Product)
    serializer_class = ProductSerializer
