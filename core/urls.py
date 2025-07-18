from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/store/', include('store.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/payment/', include('payment.urls')),
]


schema_view = get_schema_view(openapi.Info(
    title="Gadget.kg API",
    default_version='v1',
), public=True)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
