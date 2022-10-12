from guides.models import Colors, CarBrands
from orders.models import Orders


def ReportColorCount() -> list:
    """Создание словаря цвет-количество заказанных машин"""
    list_colors = []
    for color in Colors.objects.all():
        count = 0
        try:
            for order in Orders.objects.filter(color_id=color.id):
                count += order.count
        except BaseException:
            pass
        list_colors.append(
            {'color': color.color,
             'count': count}
        )
    return list_colors


def ReportBrandCount() -> list:
    """Создание словаря цвет-количество заказанных машин"""
    list_brands = []
    for brand in CarBrands.objects.all():
        count = 0
        try:
            for order in Orders.objects.filter(brand_id=brand.id):
                count += order.count
        except BaseException:
            pass
        list_brands.append(
            {'brand': brand.brand, 'count': count}
        )
    return list_brands
