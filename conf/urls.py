from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.products.urls'), name='products'),
    path('orders/', include('apps.orders.urls'), name='orders'),
    path('deliveries/', include('apps.deliveries.urls'), name='orders'),
    
]
