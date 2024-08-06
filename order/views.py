from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from home.models import Product
from .forms import AddCartForm
from .cart import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem


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
