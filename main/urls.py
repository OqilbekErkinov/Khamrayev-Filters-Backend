from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views.productView import ProductView, ProductDetailView, Filter_typeView, \
    ManafacturerView, Brands_of_equipmentView, EquipmentView
from main.views.product_filter import TypeFilter, FirmFilter
from main.views.searchView import SearchProducts
from main.views.FilterSearchView import FilterRequestView
from main.views.ContactView import ContactFormView
from main.views.OformitView import OformitProductsView

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
    path("filter-request/", FilterRequestView.as_view(), name="filter_request_api"),
    path("contact-form/", ContactFormView.as_view(), name="contact_form_api"),
    path("oformit-products/", OformitProductsView.as_view(), name="oformit_products_api"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
