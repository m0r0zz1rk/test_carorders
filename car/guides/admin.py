from django.contrib import admin

from .models import Colors, CarBrands, CarModels


@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    pass


@admin.register(CarBrands)
class ColorsAdmin(admin.ModelAdmin):
    pass


@admin.register(CarModels)
class ColorsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model')

