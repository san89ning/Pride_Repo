from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/success/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('myaccount/update_profile/', views.update_profile, name='update_profile'),
    path('seller/', views.seller, name='seller'),
    path('seller/add-product/', views.add_product, name='add_product'), 
    path('seller/edit-product/<int:pk>/', views.edit_product, name='edit_product'), 
    path('seller/delete-product/<int:pk>/', views.delete_product, name='delete_product'), 
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail')
]