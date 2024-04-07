from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Supplier
from .forms import SupplierForm 


class SupplierListView(ListView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'accounts/supplier_list.html'


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'accounts/supplier_form.html'
    success_url = reverse_lazy('accounts:supplier_list')


class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'accounts/supplier_form.html'
    success_url = reverse_lazy('accounts:supplier_list')


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'accounts/supplier_confirm_delete.html'
    success_url = reverse_lazy('accounts:supplier_list')
