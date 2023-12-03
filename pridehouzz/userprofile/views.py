from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Userprofile
from django.contrib.auth.decorators import login_required
from store.forms import ProductForm
from store.models import Product, OrderItem
from django.utils.text import slugify
from django.contrib import messages
from .forms import SignUpForm, ProfileUpdateForm, UserUpdateForm

# Create your views here.
def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status = Product.ACTIVE)
    return render(request, 'userprofile/vendor_detail.html', {
        'user' : user,
        'products': products,
    })

@login_required(login_url='login')
def seller(request):
    Products = request.user.products.exclude(status = Product.DELETED)

    return render(request, 'userprofile/seller.html', {
        'products': Products
    })

@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            title = request.POST.get('title')

            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, 'Product was added successfully')

            return redirect('seller')
    else:

        form = ProductForm()

    return render(request, 'userprofile/add_product.html', {
        'title': 'Add product',
        'form': form
    })

@login_required(login_url='login')
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            messages.success(request, 'Product was updated successfully')

            return redirect('seller')
    else:
        form = ProductForm(instance=product)

    return render(request, 'userprofile/add_product.html', {
        'title': 'Edit product',
        'product': product,
        'form': form
    })

@login_required(login_url='login')
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()

    messages.success(request, 'Product was deleted successfully')

    return redirect('seller')

@login_required(login_url='login')
def myaccount(request):
    user = request.user
    orderitem = OrderItem.objects.all()
    return render(request, 'userprofile/myaccount.html', {
        'user': user,
        'orderitem': orderitem,
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            phone_number = form.cleaned_data.get('phone_number')
            user = User.objects.get(username=username)
            userprofile = Userprofile.objects.create(user=user, username=username, phone_number=phone_number)
            userprofile.save()
            login(request, user)
            
            return render(request, 'userprofile/signup_success.html')
    else:
        form = SignUpForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })

@login_required
def update_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your profile is updated successfully!')
            return redirect('update_profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
        u_form = UserUpdateForm(instance=request.user.userprofile)

    context = {'p_form': p_form, 'u_form': u_form}  
    return render(request, 'userprofile/update_profile.html', context)