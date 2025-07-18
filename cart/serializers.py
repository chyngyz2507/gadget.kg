from rest_framework import serializers
from .models import ShoppingCart, ShoppingCartItem

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ['id', 'cart', 'item', 'quantity']
        read_only_fields = ['cart']

class ShoppingCartSerializer(serializers.ModelSerializer):
    items = ShoppingCartItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ['id', 'user', 'created_at', 'items']
        read_only_fields = ['user']
