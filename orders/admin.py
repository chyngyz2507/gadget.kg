from django.contrib import admin

from orders.models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'status']

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'item', 'quantity', 'price_at_purchase']

admin.site.register(OrderItem,OrderItemAdmin)