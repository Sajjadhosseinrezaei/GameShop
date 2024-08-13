from django.db import models


class OrderManager(models.Manager):
    def get_sold_products(self, start_date, end_date):
        output = self.model.objects.filter(paid=True,
                                           updated__range=(start_date, end_date)
                                           ).select_related('items__product').values(
            'user__full_name',
            'items__product__name',
            'items__quantity'
        )
        return output
