from django.db import models
import os
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='ریر دسته',
                                     related_name='scategory', null=True, blank=True,
                                     help_text='با کلیک بر روی دکمه اضافه کردن دسته بندی، می توانید دسته بندی های جدید را ایجاد کرده و همچنین با زدن تیک گزینه ایجاد زیر دسته، برای دسته بندی های ساخته شده یک زیر دسته ایجاد کنید!')
    name = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    is_sub = models.BooleanField(default=False, verbose_name='زیر دسته؟')
    slug = models.SlugField(verbose_name='اسلاگ')

    class Meta:
        ordering = ['name']
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category', args=[self.slug,])


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام کامل')
    slug = models.SlugField(verbose_name='اسلاگ')
    price = models.IntegerField(verbose_name='قیمت')
    category = models.ManyToManyField(Category,verbose_name='دسته بندی',  related_name='pcategory')
    image = models.ImageField(upload_to='Product/image', verbose_name='عکس')
    description = models.CharField(verbose_name='توضیحات')
    available = models.BooleanField(default=True, verbose_name='در دسترس')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, blank=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        ordering = ['-created']
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name




