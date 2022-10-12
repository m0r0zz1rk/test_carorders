from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .models import Orders
from .serializers import OrdersReadSerializer, OrdersCUDSerializer, ReportColorCountSerializer, \
    ReportBrandCountSerializer
from .views import ReportColorCount, ReportBrandCount


class OrdersReadViewSet(viewsets.ModelViewSet):
    """Получение списка заказов/детальной информации о заказе"""
    serializer_class = OrdersReadSerializer
    queryset = Orders.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend,
                       OrderingFilter]
    filterset_fields = ['brand',]
    ordering_fields = ['count',]


class OrdersCUDViewSet(viewsets.ModelViewSet):
    """Create, update, delete заказов"""
    serializer_class = OrdersCUDSerializer
    queryset = Orders.objects.all().order_by('-id')

    def create(self, request, *args, **kwargs):
        if request.data.get('date_order') is None:
            date_now = datetime.now().strftime('%d.%m.%Y')
            request.data.update({'date_order': date_now})
        serialize = self.serializer_class(
            data=request.data
        )
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        order = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        serialize = self.serializer_class(
            order,
            data=request.data,
        )
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        order = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        try:
            order.delete()
            return Response(status=status.HTTP_200_OK)
        except BaseException:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ReportsViewSet(viewsets.ViewSet):
    """Получение отчета по количеству заказанных авто каждого цвета/марки"""

    def get_reportcolor(self, request):
        list = ReportColorCount()
        serialize = ReportColorCountSerializer(data=list, many=True)
        if serialize.is_valid(raise_exception=True):
            return Response(data=serialize.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def get_reportbrand(self, request):
        list = ReportBrandCount()
        serialize = ReportBrandCountSerializer(data=list, many=True)
        if serialize.is_valid(raise_exception=True):
            return Response(data=serialize.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


