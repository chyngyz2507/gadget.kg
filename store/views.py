from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, SubCategory, Item, Review
from .serializers import (
    CategorySerializer,
    SubCategorySerializer,
    ItemSerializer,
    ReviewSerializer
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['subcategory__category', 'subcategory', 'price', 'count']

    search_fields = ['title', 'description']

    ordering_fields = ['price', 'count', 'id']


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        item_id = self.request.query_params.get('item')
        if item_id:
            return Review.objects.filter(item__id=item_id)
        return Review.objects.all()
