from django.db import models


class Colors(models.Model):
    """Модель цветов автомобилей"""
    color = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Цвет'
    )

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class CarBrands(models.Model):
    """Модель марок автомобилей"""
    brand = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Марка'
    )

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"


class CarModels(models.Model):
    """Модель моделей марок автомобилей"""
    brand = models.ForeignKey(
        CarBrands,
        on_delete=models.CASCADE,
        default='',
        null=False,
        verbose_name='Марка'
    )
    model = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Модель'
    )

    def MarkModel(self):
        return f'{self.brand} {self.model}'

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        unique_together = ('brand', 'model')