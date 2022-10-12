from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/guides/', include('guides.urls')),
    path('api/orders/', include('orders.urls')),
]

urlpatterns += docs_urls
