from django.shortcuts import render, redirect
from store.models import Product, Category, Brand, Size
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from store.cart import Cart

# Create your views here.
def home(request):
    try:
        products = Product.objects.filter(status = Product.ACTIVE)[0:4]
        category = Category.objects.all()
        cart = Cart(request)

        context = {
            'products': products,
            'category': category,
            'cart': cart,
        }

        return render(request, 'core/home.html', context)
    except ObjectDoesNotExist as e:
        return HttpResponse(f"An error occurred: {str(e)}")
    except Exception as e:
        return HttpResponse(f"An unexpected error occurred: {str(e)}")

def about(request):
    cart = Cart(request)

    context = {
        'cart': cart,
    }

    return render(request, 'core/about.html', context)

def product(request):
    products = Product.objects.filter(status = Product.ACTIVE)
    category = Category.objects.all()
    brand = Brand.objects.all()
    size = Size.objects.all()
    cart = Cart(request)
    

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 4)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'category': category,
        'brand': brand,
        'size': size,
        'cart': cart,
    }

    return render(request, 'core/product.html', context)

@login_required
def construction(request):
    total = 0
    category = Category.objects.all()
    brand = Brand.objects.all()
    size = Size.objects.all()
    cart = Cart(request)

    if request.method == 'GET':
        area = request.GET.get('area')

        if area:
            iron = int(area) * 2400
            roofing_sheet = int(area) * 1200
            wages = int(area) * 25
            total = iron + roofing_sheet + wages

        context = {
            'area': area,
            'total': total,
            'category': category,
            'brand': brand,
            'size': size,
            'cart': cart,
            }

    return render(request, 'core/construction.html', context)

def contact(request):
    category = Category.objects.all()
    cart = Cart(request)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')

    form = ContactForm()
    return render(request, "core/contact.html", {
        'form': form,
        'category': category,
        'cart': cart,
    })

def privacy(request):
    return render(request, "core/privacy.html")

def product_return(request):
    return render(request, "core/return.html")

def payment(request):
    return render(request, "core/payment.html")

def delivery(request):
    return render(request, "core/delivery.html")