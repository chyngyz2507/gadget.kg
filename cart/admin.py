from django.contrib import admin

from cart.models import ShoppingCart, ShoppingCartItem


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']


admin.site.register(ShoppingCart, ShoppingCartAdmin)

class ShoppingCartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'item', 'quantity']

admin.site.register(ShoppingCartItem, ShoppingCartItemAdmin)
