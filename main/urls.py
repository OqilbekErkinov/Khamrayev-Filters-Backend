from django.urls import path
from main.views.productView import ProductView
urlpatterns = [
        path('api/products/', ProductView.as_view(), name='product-list'),
]