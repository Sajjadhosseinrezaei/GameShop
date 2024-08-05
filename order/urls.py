from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('cart/detail/', views.CartDetailView.as_view(), name='cart_detail'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
]