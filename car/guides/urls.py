from django.urls import path

from .api_views import ColorCRUDViewSet, CarBrandsCRUDViewSet, CarModelsCRUDViewSet

urlpatterns = [
    path('color_create/', ColorCRUDViewSet.as_view({'post': 'create'})),
    path('colors/', ColorCRUDViewSet.as_view({'get': 'list'})),
    path('color/<int:pk>', ColorCRUDViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),

    path('brand_create/', CarBrandsCRUDViewSet.as_view({'post': 'create'})),
    path('brands/', CarBrandsCRUDViewSet.as_view({'get': 'list'})),
    path('brand/<int:pk>', CarBrandsCRUDViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),

    path('model_create/', CarModelsCRUDViewSet.as_view({'post': 'create'})),
    path('models/', CarModelsCRUDViewSet.as_view({'get': 'list'})),
    path('model/<int:pk>', CarModelsCRUDViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),
]