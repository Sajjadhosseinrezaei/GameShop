from django.shortcuts import render
from django.views import View
from .models import Product
from django.shortcuts import get_object_or_404
from order.forms import AddCartForm


# Create your views here.
class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})


class ProductDetailView(View):
    template_name = 'home/detail.html'

    def get(self, request, p_slug):
        form = AddCartForm
        product = get_object_or_404(Product, slug=p_slug)
        return render(request, self.template_name, {'product': product, 'form': form})



