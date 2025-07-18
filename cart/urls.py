from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ShoppingCartViewSet, ShoppingCartItemViewSet

router = DefaultRouter()
router.register(r'carts', ShoppingCartViewSet, basename='cart')
router.register(r'cart-items', ShoppingCartItemViewSet, basename='cartitem')

urlpatterns = router.urls
