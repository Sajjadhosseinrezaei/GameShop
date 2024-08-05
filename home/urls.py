from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<slug:p_slug>/', views.ProductDetailView.as_view(), name='detail'),
]
