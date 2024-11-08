from django.db import models


class OrderManager(models.Manager):
    def get_sold_products(self, start_date, end_date):
        output = self.model.objects.filter(paid=True,
                                           updated__range=(start_date, end_date)
                                           ).select_related('items__product').values(
            'user__name',
            'user__family',
            'items__product__name',
            'items__quantity',
            'updated'
        )
        return output
