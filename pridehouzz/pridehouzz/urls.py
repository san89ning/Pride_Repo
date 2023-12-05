"""
URL configuration for pridehouzz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home, about, product, contact, construction, privacy, product_return, payment, delivery
from store.views import category_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('construction/', construction, name='construction'),
    path('contact/', contact, name='contact'),
    path('privacy/', privacy, name='privacy'),
    path('return/', product_return, name='return'),
    path('payment/', payment, name='payment'),
    path('delivery/', delivery, name='delivery'),
    path('', include('userprofile.urls')),
    path('', include('store.urls'))
] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)