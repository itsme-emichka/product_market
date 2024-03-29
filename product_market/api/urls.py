from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register('product', viewset=views.ProductViewSet)
router.register('category', viewset=views.CategoryViewSet, basename='category')
router.register('cart', viewset=views.CartViewSet, basename='cart')


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
