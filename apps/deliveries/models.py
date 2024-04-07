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

    class Meta:
        verbose_name = "Поставка"
        verbose_name_plural = "Поставки"
        ordering = ['-expected_arrival']
        
        
class DeliveryProduct(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Продукт поставки"
        verbose_name_plural = "Продукты поставки"
        ordering = ['delivery']
        
    def save(self, *args, **kwargs):
        if self.pk is None:  # Если объект создается впервые
            self.product.stock += self.quantity  # Увеличиваем запас на количество из поставки
            self.product.save()
        else:
            # Если объект обновляется, корректируем запас на разницу между старым и новым количеством
            old_quantity = DeliveryProduct.objects.get(pk=self.pk).quantity
            difference = self.quantity - old_quantity
            self.product.stock += difference
            self.product.save()
        super(DeliveryProduct, self).save(*args, **kwargs)