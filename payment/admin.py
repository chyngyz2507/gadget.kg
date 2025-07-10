from django.contrib import admin

from payment.models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'amount', 'payment_method', 'payment_status', 'paid_at']

admin.site.register(Payment, PaymentAdmin)