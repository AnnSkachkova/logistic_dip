from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', include('apps.products.urls'), name='products'),
    path('orders/', include('apps.orders.urls'), name='orders'),
    path('deliveries/', include('apps.deliveries.urls'), name='deliveries'),
    path('accounts/', include('apps.accounts.urls'), name='accounts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)