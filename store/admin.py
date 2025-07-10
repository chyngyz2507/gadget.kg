from django.contrib import admin
from .models import Category, SubCategory, Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']

admin.site.register(SubCategory, SubCategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'image', 'price', 'count', 'subcategory']

admin.site.register(Item, ItemAdmin)