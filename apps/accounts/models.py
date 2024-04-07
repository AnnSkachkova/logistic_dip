from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    # Дополнительные поля

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    # Другие поля
    
    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ['name']
