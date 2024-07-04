from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.db.models import Q
from .cart import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def menu(request):
    items = Item.objects.filter(status='active')
    return render(request, 'menu.html',{
        'items':items
    })

def category_detail(request,slug):
    category = get_object_or_404(Category, slug=slug)
    items = category.Items.all()
    print(category,items)
    return render(request, 'category_detail.html', {
        'category':category,
        'items':items
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            userprofile = UserProfile.objects.create(user=user)
            return redirect('home')
        else:
            messages.success(request, form.errors)

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {
        'form': form
    })

@login_required
def myaccount(request):
    user=request.user
    return render(request, 'myaccount.html',{
        'user':user
    })

def search(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(Q(title__icontains=query) | Q(description__icontains= query))
    print(items)
    return render(request, 'search.html', {
        'query':query,
        'items':items
    })

##############  CART  #####################
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('menu')
    
@login_required   
def cart_view(request):
    cart = Cart(request)

    return render(request, 'cart_view.html',{
            'cart':cart
    })
def change_quantity(request, product_id):
    action = request.GET.get('action', '')

    if action:
        quantity =1

        if action == 'decrease':
            quantity = -1 

        cart = Cart(request)
        cart.add(product_id,quantity, True)
    return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(str(product_id))
    return redirect('cart_view')