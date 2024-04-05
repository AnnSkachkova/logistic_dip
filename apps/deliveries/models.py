from django.db import models
from apps.products.models import Product
from apps.accounts.models import Supplier  # Предполагая, что модель Supplier теперь в приложении accounts


class Delivery(models.Model):
    STATUS_CHOICES = (
        ('ordered', 'Ordered'),
        ('shipped', 'Shipped'),
        ('received', 'Received'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ordered')
    expected_arrival = models.DateField()
    actual_arrival = models.DateField(null=True, blank=True)

class DeliveryProduct(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
