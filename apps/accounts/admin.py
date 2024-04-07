from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Supplier

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'phone_number', 'is_staff', ]  # добавьте 'phone_number' и любые другие пользовательские поля
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),  # Добавьте 'phone_number' и любые другие пользовательские поля в раздел админки
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),  # Добавьте 'phone_number' и любые другие пользовательские поля при создании пользователя
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_info']  # Отображаемые поля в списке поставщиков
    search_fields = ['name']  # Поля, по которым можно выполнять поиск поставщиков