from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = router.urls
