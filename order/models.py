from django.db import models
from home.models import Product
from django.contrib.auth import get_user_model


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='order')
    address = models.CharField(verbose_name="آدرس")
    is_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.user}'

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id}'

    def cost(self):
        return self.price * self.quantity
