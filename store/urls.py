from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, ItemViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]