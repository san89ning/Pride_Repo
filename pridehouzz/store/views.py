from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Brand, Size
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import SearchTerm, OrderItem
from .cart import Cart
from .forms import OrderForm
import requests

# Create your views here.

@login_required
def search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        user = request.user  

        if user:
            st, _ = SearchTerm.objects.get_or_create(
                defaults={'query':query, 'user':user},
                query__iexact = query
            )
            st.no_of_searches += 1
            st.save()

        products = Product.objects.filter(status = Product.ACTIVE).filter(
            Q(title__icontains = query)
            |
            Q(description__icontains = query)
        )

    return render(request, 'store/search.html', {
        'query': query,
        'products': products,
    })

@login_required(login_url='login')
def category_detail(request, slug):

    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)

    category = Category.objects.all()
    brand = Brand.objects.all()
    size = Size.objects.all()

    return render(request, 'store/category_detail.html', {
        'category': category,
        'brand': brand,
        'size': size,
        'products': products
    })

@login_required(login_url='login')
def category_product(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)

    return render(request, 'store/product_detail.html', {
        'product': product
    })

@login_required(login_url='login')
def brand_detail(request, slug):
    brand = get_object_or_404(Brand, slug=slug)
    products = brand.products.filter(status=Product.ACTIVE)

    category = Category.objects.all()
    brand = Brand.objects.all()
    size = Size.objects.all()

    return render(request, 'store/brand_detail.html', {
        'category': category,
        'brand': brand,
        'size': size,
        'products': products
    })

@login_required(login_url='login')
def brand_product(request, brand_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)

    return render(request, 'store/product_detail.html', {
        'product': product
    })

@login_required(login_url='login')
def size_detail(request, slug):
    size = get_object_or_404(Size, slug=slug)
    products = size.products.filter(status=Product.ACTIVE)

    category = Category.objects.all()
    brand = Brand.objects.all()
    size = Size.objects.all()

    return render(request, 'store/size_detail.html', {
        'category': category,
        'brand': brand,
        'size': size,
        'products': products
    })

@login_required(login_url='login')
def size_product(request, size_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)

    return render(request, 'store/product_detail.html', {
        'product': product
    })

@login_required
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart_view')

def success(request):
    return render(request, 'store/success.html')

@login_required
def cart_view(request):
    cart = Cart(request)
    products = Product.objects.filter(status = Product.ACTIVE)[0:4]

    return render(request, 'store/cart_view.html', {
        'cart': cart,
        'products': products,
    })

@login_required
def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            total_price = 0

            for item in cart:
                product = item['product']
                total_price += product.price * int(item['quantity'])

            order = form.save(commit=False)
            order.created_by = request.user
            order.amount = total_price
            order.save()

            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            cart.clear()

            return render(request, 'store/order_success.html')
    else:
        form = OrderForm()

    return render(request, 'store/checkout.html', {
        'cart': cart,
        'form': form,
    })

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')

def change_quantity(request, product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1

        cart = Cart(request)
        cart.add(product_id, quantity, True)
    
    return redirect('cart_view')
