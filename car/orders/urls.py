from django.urls import path

from orders.api_views import OrdersReadViewSet, OrdersCUDViewSet, ReportsViewSet

urlpatterns = [
    path('order_create/', OrdersCUDViewSet.as_view({'post': 'create'})),
    path('orders/', OrdersReadViewSet.as_view({'get': 'list'})),
    path('order/<int:pk>', OrdersReadViewSet.as_view({'get': 'retrieve'})),
    path('order_ud/<int:pk>', OrdersCUDViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),

    path('report_color/', ReportsViewSet.as_view({'get': 'get_reportcolor'})),
    path('report_brand/', ReportsViewSet.as_view({'get': 'get_reportbrand'})),
]