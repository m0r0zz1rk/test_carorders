from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Colors, CarBrands, CarModels
from .serializers import ColorsSerializer, CarBrandsSerializer, CarModelsSerializer


class ColorCRUDViewSet(viewsets.ModelViewSet):
    """CRUD цвета автомобилей"""
    serializer_class = ColorsSerializer
    queryset = Colors.objects.all().order_by('-id')

    def create(self, request, *args, **kwargs):
        serialize = self.serializer_class(
            data=request.data
        )
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        color = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        serialize = self.serializer_class(
            color,
            data=request.data,
        )
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        color = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        try:
            color.delete()
            return Response(status=status.HTTP_200_OK)
        except BaseException:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CarBrandsCRUDViewSet(viewsets.ModelViewSet):
    """CRUD марки автомобилей"""
    serializer_class = CarBrandsSerializer
    queryset = CarBrands.objects.all().order_by('-id')

    def create(self, request, *args, **kwargs):
        serialize = self.serializer_class(
            data=request.data
        )
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        brand = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        serialize = self.serializer_class(
            brand,
            data=request.data,
        )
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        brand = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        try:
            brand.delete()
            return Response(status=status.HTTP_200_OK)
        except BaseException:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CarModelsCRUDViewSet(viewsets.ModelViewSet):
    """CRUD моделей марок автомобилей"""
    serializer_class = CarModelsSerializer
    queryset = CarModels.objects.all().order_by('-id')

    def create(self, request, *args, **kwargs):
        serialize = self.serializer_class(
            data=request.data
        )
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        model = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        serialize = self.serializer_class(
            model,
            data=request.data,
        )
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        model = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        try:
            model.delete()
            return Response(status=status.HTTP_200_OK)
        except BaseException:
            return Response(status=status.HTTP_400_BAD_REQUEST)

