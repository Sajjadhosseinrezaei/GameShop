from django.db import models
from home.models import Product
from django.contrib.auth import get_user_model
from .managers import OrderManager


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='order', verbose_name='کاربر')
    paid = models.BooleanField(default=False, verbose_name='پرداخت')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')

    objects = OrderManager()

    class Meta:
        ordering = ['paid', '-created']
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def __str__(self):
        return f'{self.id} {self.user}'

    def get_total_price(self):
        total = sum(item.cost() for item in self.items.all())
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='سفارش')
    price = models.IntegerField(verbose_name='قیمت')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.IntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name = 'آیتم سفارش'
        verbose_name_plural = 'آیتم های سفارش'

    def __str__(self):
        return f'{self.id}'

    def cost(self):
        return self.price * self.quantity
