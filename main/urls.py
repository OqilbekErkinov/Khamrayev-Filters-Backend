from django.urls import path
from main.views.productView import ProductView, ProductDetailView
urlpatterns = [
        path('products', ProductView.as_view(), name='product-list'),
        path('products/<int:product_id>/', ProductDetailView.as_view(), name='product-detail'),
]