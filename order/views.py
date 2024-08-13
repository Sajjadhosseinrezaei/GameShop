from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from home.models import Product
from .forms import AddCartForm, OutputForm
from .cart import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from django.contrib import messages
import csv


# Create your views here.
class CartDetailView(View):
    template_name = 'order/cart.html'

    def get(self, request):
        cart = Cart(request)
        return render(request, self.template_name, {'cart': cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        form = AddCartForm(request.POST)
        product = get_object_or_404(Product, id=product_id)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('order:cart_detail')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('order:cart_detail')


class OrderDetailView(LoginRequiredMixin, View):
    template_name = 'order/order_detail.html'

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, self.template_name, {'order': order})


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, price=item['price'],
                                     product=item['product'],
                                     quantity=item['quantity'])
            cart.clear()
        return redirect('order:detail_order', order.id)


class OrderPayView(LoginRequiredMixin, View):
    template_name = 'order/payment.html'

    def dispatch(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['order_id'])
        if order.get_total_price() <= 0:
            messages.success(request, "سبد خرید خالی است")
            return redirect('order:cart_detail')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, self.template_name, {'order': order})


class OrderPayVerifyView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order.paid = True
        order.save()
        messages.success(request, "پرداخت با موفقیت انجام شد")
        return redirect('home:home')


class OrderReportView(LoginRequiredMixin, View):
    template_name = 'order/order_report.html'

    def get(self, request):
        form = OutputForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = OutputForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            result = Order.objects.get_sold_products(start_date, end_date)
            fieldnames = result[0].keys()
            path = r"C:\report\report.csv"
            with open(path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()

                for row in result:
                    writer.writerow(row)
                messages.success(request, 'گزارش تهیه شد')
                return redirect('home:home')
        return render(request, self.template_name, {'form': form})
