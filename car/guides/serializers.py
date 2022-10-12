from rest_framework import serializers

from .models import Colors, CarBrands, CarModels


class ColorsSerializer(serializers.ModelSerializer):
    """Сериализация полей модели цветов автомобилей"""

    class Meta:
        model = Colors
        fields = '__all__'


class CarBrandsSerializer(serializers.ModelSerializer):
    """Сериализация полей модели марок автомобилей"""

    class Meta:
        model = CarBrands
        fields = '__all__'


class CarModelsSerializer(serializers.ModelSerializer):
    """Сериализация полей модели моделей автомобилей"""
    brand = serializers.SlugRelatedField(slug_field='brand', queryset=CarBrands.objects.all())

    class Meta:
        model = CarModels
        fields = '__all__'