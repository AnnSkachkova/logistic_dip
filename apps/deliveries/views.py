from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from .models import Delivery
from .forms import DeliveryForm, DeliveryProductFormset


class DeliveryListView(ListView):
    model = Delivery
    context_object_name = 'deliveries'
    template_name = 'deliveries/delivery_list.html'

class DeliveryCreateView(CreateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'deliveries/delivery_form.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class()
        delivery_product_formset = DeliveryProductFormset()
        return self.render_to_response(self.get_context_data(form=form, delivery_product_formset=delivery_product_formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class(request.POST)
        delivery_product_formset = DeliveryProductFormset(request.POST)
        if form.is_valid() and delivery_product_formset.is_valid():
            return self.form_valid(form, delivery_product_formset)
        else:
            return self.form_invalid(form, delivery_product_formset)

    def form_valid(self, form, delivery_product_formset):
        self.object = form.save()
        delivery_product_formset.instance = self.object
        delivery_product_formset.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, delivery_product_formset):
        return self.render_to_response(self.get_context_data(form=form, delivery_product_formset=delivery_product_formset))

    def get_success_url(self):
        return reverse_lazy('deliveries:delivery_list')


class DeliveryUpdateView(UpdateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'deliveries/delivery_form.html'

    # Аналогичная логика обработки GET и POST запросов, как в DeliveryCreateView

class DeliveryDeleteView(DeleteView):
    model = Delivery
    template_name = 'deliveries/delivery_confirm_delete.html'
    success_url = reverse_lazy('deliveries:delivery_list')
