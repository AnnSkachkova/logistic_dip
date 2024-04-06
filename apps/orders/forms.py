from django import forms
from django.forms import inlineformset_factory
from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'status']

# Создание формсета для элементов заказа
OrderItemFormset = inlineformset_factory(
    parent_model=Order,
    model=OrderItem,
    fields=['product', 'quantity'],
    extra=1, 
    can_delete=True 
)
