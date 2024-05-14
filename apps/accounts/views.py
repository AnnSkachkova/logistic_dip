from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Supplier, Token
from .forms import SupplierForm 


class LoginView(LoginView):
    template_name = 'auth/login.html'
    
    def get_success_url(self) -> str:
        user = self.request.user
        token = self.request.POST['user_token']
        Token.objects.update_or_create(user=user, defaults={'token': token})
        return reverse('accounts:supplier_list')
    

class Logout(LogoutView):
    next_page = reverse_lazy('login')


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
