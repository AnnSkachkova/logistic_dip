from django.db import models
from django.conf import settings
from apps.products.models import Product


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'В ожидании'),
        ('completed', 'Завершён'),
        ('cancelled', 'Отменён'),
    )
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']
        

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказов"
        ordering = ['order']