from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('change-quantity/<str:product_id>/', views.change_quantity, name='change_quantity'),
    path('remove-from-cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('cart/checkout/order_success/', views.checkout, name='checkout'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('category/<slug:category_slug>/<slug:slug>/', views.category_product, name='category_product'),
    path('brand/<slug:slug>/', views.brand_detail, name='brand_detail'),
    path('brand/<slug:brand_slug>/<slug:slug>/', views.brand_product, name='brand_product'),
    path('size/<slug:slug>/', views.size_detail, name='size_detail'),
    path('size/<slug:size_slug>/<slug:slug>/', views.size_product, name='size_product')
]