from django import forms
from django.forms import inlineformset_factory
from .models import Delivery, DeliveryProduct


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['supplier', 'status', 'expected_arrival', 'actual_arrival']

DeliveryProductFormset = inlineformset_factory(
    Delivery, DeliveryProduct,
    fields=['product', 'quantity'],
    extra=1, can_delete=True
)
