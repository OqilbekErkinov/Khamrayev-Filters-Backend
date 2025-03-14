from django.urls import path
from main.views.productView import ProductView, ProductDetailView, Filter_typeView, \
    ManafacturerView, Brands_of_equipmentView, EquipmentView
from main.views.product_filter import TypeFilter, FirmFilter
from main.views.searchView import SearchProducts

urlpatterns = [
    path('products', ProductView.as_view(), name='product-list'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product-detail'),
    path('filter-types', Filter_typeView.as_view(), name='filter-type-list'),
    path('manafacturers', ManafacturerView.as_view(), name='manafacturer-list'),
    path('brands_of_equipments', Brands_of_equipmentView.as_view(), name='brands_of_equipment-list'),
    path('equipments', EquipmentView.as_view(), name='equipment-list'),
    path('productstypefilter/', TypeFilter.as_view(), name='product-filter-by-type'),
    path('productsfirmfilter/', FirmFilter.as_view(), name='product-filter-by-firm'),
    path('search_products/', SearchProducts.as_view(), name='search_products'),

]
