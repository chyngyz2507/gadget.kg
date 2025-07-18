from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import ShoppingCart, ShoppingCartItem
from .serializers import ShoppingCartSerializer, ShoppingCartItemSerializer

class ShoppingCartViewSet(ModelViewSet):
    serializer_class = ShoppingCartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShoppingCartItemViewSet(ModelViewSet):
    serializer_class = ShoppingCartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ShoppingCartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        cart, _ = ShoppingCart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)
