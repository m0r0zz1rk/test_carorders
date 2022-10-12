from datetime import datetime

from django.db import models

from guides.models import Colors, CarModels, CarBrands


class Orders(models.Model):
    """Модель заказов"""
    date_order = models.DateField(
        default=datetime.now(),
    )
    color = models.ForeignKey(
        Colors,
        on_delete=models.CASCADE,
        default='',
        null=False,
        verbose_name='Цвет'
    )
    brand = models.ForeignKey(
        CarBrands,
        on_delete=models.CASCADE,
        default='',
        null=False,
        verbose_name='Марка'
    )
    model = models.ForeignKey(
        CarModels,
        on_delete=models.CASCADE,
        default='',
        null=False,
        verbose_name='Модель'
    )
    count = models.PositiveIntegerField(
        verbose_name='Количество'
    )

    def __str__(self):
        return f'Заказ от {self.date_order.strftime("%d.%m.%Y")} на {self.model.MarkModel()}, ' \
               f'цвет "{self.color}" в количестве {self.count} шт.'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


