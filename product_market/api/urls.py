from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register('products', viewset=views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls))
]
