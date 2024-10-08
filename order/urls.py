from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('cart/detail/', views.CartDetailView.as_view(), name='cart_detail'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
    path('detail_order/<int:order_id>/', views.OrderDetailView.as_view(), name='detail_order'),
    path('create_order/', views.OrderCreateView.as_view(), name='create_order'),
    path('pay/<int:order_id>/', views.OrderPayView.as_view(), name='order_pay'),
    path('pay_verify/<int:order_id>/', views.OrderPayVerifyView.as_view(), name='order_verify'),
    path('report/', views.OrderReportView.as_view(), name='order_report'),
]
