from rest_framework import serializers

from guides.models import Colors, CarBrands
from orders.models import Orders


class OrdersReadSerializer(serializers.ModelSerializer):
    """Сериализация заказов"""
    model = serializers.SerializerMethodField('get_model')
    color = serializers.SlugRelatedField(slug_field='color', queryset=Colors.objects.all())
    date_order = serializers.DateField(format='%d.%m.%Y')

    def get_model(self, obj):
        return f'{obj.model.brand} {obj.model.model}'

    class Meta:
        model = Orders
        fields = ('id', 'date_order', 'color', 'model', 'count')


class OrdersCUDSerializer(serializers.ModelSerializer):
    """Create, update, delete заказов"""
    color = serializers.SlugRelatedField(slug_field='color', queryset=Colors.objects.all())
    brand = serializers.SlugRelatedField(slug_field='brand', queryset=CarBrands.objects.all())
    model = serializers.CharField(source='model.model')

    class Meta:
        model = Orders
        fields = '__all__'


class ReportColorCountSerializer(serializers.Serializer):
    """Сериализация данных отчета по количеству заказнных авто каждого цвета"""
    color = serializers.CharField()
    count = serializers.IntegerField()


class ReportBrandCountSerializer(serializers.Serializer):
    """Сериализация данных отчета по количеству заказанных авто каждой марки"""
    brand = serializers.CharField()
    count = serializers.IntegerField()

