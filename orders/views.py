from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from cart.models import ShoppingCartItem

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        items = ShoppingCartItem.objects.filter(cart__user=user)
        if not items.exists():
            return Response({'detail':'Корзина пуста'}, status=status.HTTP_400_BAD_REQUEST)
        total = sum(i.quantity * i.item.price for i in items)
        order = Order.objects.create(user=user, total_price=total)
        for i in items:
            order.items.create(item=i.item, quantity=i.quantity, price=i.item.price)
        items.delete()
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
