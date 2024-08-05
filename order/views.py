from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from home.models import Product
from .forms import AddCartForm
from .cart import Cart


# Create your views here.
class CartDetailView(View):
    template_name = 'order/cart.html'

    def get(self, request):
        return render(request, self.template_name)


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        form = AddCartForm(request.POST)
        product = get_object_or_404(Product, id=product_id)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('order:cart_detail')

