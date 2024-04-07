from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order

@receiver(pre_save, sender=Order)
def update_stock_on_order_completed(sender, instance, **kwargs):
    if instance.pk:
        old_order = Order.objects.get(pk=instance.pk)
        if old_order.status != 'completed' and instance.status == 'completed':
            # Обрабатываем изменение статуса заказа на "completed"
            for item in instance.items.all():
                item.product.stock -= item.quantity
                item.product.save()
