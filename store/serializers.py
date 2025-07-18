from rest_framework import serializers
from .models import Category, SubCategory, Item
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'item', 'rating', 'comment', 'created_at']
        read_only_fields = ['user']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'description', 'image', 'count', 'subcategory', 'average_rating', 'reviews']

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return None

