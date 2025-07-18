from django.db import models
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='items/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')
        ordering = ['-created_at']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.user.email} - {self.item.title} - {self.rating}"
