from http import HTTPMethod

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from api.services import (
    get_all_objects,
    add_product_to_cart,
    delete_product_from_cart,
    edit_product_amount,
)
from api.utils import get_category_parent_and_children


class ProductViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):
    queryset = get_all_objects(Product)
    serializer_class = ProductSerializer

    @action(
            methods=(HTTPMethod.POST, HTTPMethod.DELETE, HTTPMethod.PATCH,),
            detail=True,
            permission_classes=(IsAuthenticated,),
        )
    def cart(self, request: Request, pk: int = None) -> Response:
        if request.method == HTTPMethod.POST:
            amount: str = self.request.query_params.get('amount', '1')
            if not amount.isdigit():
                return Response(
                    {'detail': 'Количество должно быть числом'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            cart_position = add_product_to_cart(
                request.user,
                pk,
                int(amount),
            )
            return Response(
                {'detail': (
                    'Товар добавлен. ' +
                    f'Сейчас в корзине {cart_position.amount}')},
                status=status.HTTP_200_OK,
            )

        if request.method == HTTPMethod.DELETE:
            delete_product_from_cart(request.user, pk)
            return Response(
                {'detail': 'Товар удален'},
                status=status.HTTP_204_NO_CONTENT,
            )

        if request.method == HTTPMethod.PATCH:
            amount: str = self.request.query_params.get('amount', None)
            if not amount:
                return Response(
                    {'detail': 'Введите количество в параметрах запроса'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if not amount.isdigit():
                return Response(
                    {'detail': 'Количество должно быть числом'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            cart_position = edit_product_amount(
                request.user,
                pk,
                int(amount)
            )
            return Response(
                {'detail': (
                    'Количество обновлено. ' +
                    f'Сейчас в корзине {cart_position.amount}')},
                status=status.HTTP_200_OK,
            )


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
