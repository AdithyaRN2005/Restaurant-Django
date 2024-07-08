from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category, UserProfile, Order, OrderItem, Address
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.db.models import Q
from .cart import Cart
from .forms import CheckOutForm, EditProfileForm, AddAddressForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def menu(request):
    items = Item.objects.filter(status='active')
   
    return render(request, 'menu.html', {
        'items': items,
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
    user=UserProfile.objects.get(user=request.user)
    addresses = Address.objects.filter(user_profile=request.user)
    order_records = Order.objects.filter(purchased_by=request.user)[:3]

    if request.method == 'POST':
        edit_prof_form = EditProfileForm(request.POST, instance=user)
        if edit_prof_form.is_valid():
            edit_prof_form.save()
            return render(request, 'myaccount.html', {
                'user': user,
                'addresses':addresses,
                'order_records':order_records,
                'edit_prof_form': edit_prof_form,
                'success_message': 'Your profile has been updated successfully.'
            })
        else:
            print("Form errors:", edit_prof_form.errors)
        # If form is not valid, handle errors (e.g., display errors in the form)
    else:
        edit_prof_form = EditProfileForm(instance=user)
    for address in addresses:
        print(address)
    return render(request, 'myaccount.html', {
        'user': user,
        'addresses':addresses,
        'order_records':order_records,
        'edit_prof_form': edit_prof_form,
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

def buy_now(request,address_id=1):
    cart = Cart(request)
    user=UserProfile.objects.get(user=request.user)
    order_records = Order.objects.filter(purchased_by=request.user)[:3]


    if request.method == 'POST':
        form = CheckOutForm(request.POST, instance=user, user=request.user)
        if form.is_valid():
            form.save()
            total_bill = cart.get_total_cost()
            address_id = form.cleaned_data['address_id'].id
            user_address = Address.objects.get(pk=address_id)
            order = Order.objects.create(
                purchased_by=request.user,
                purchased_at=timezone.now(),
                email=user.email,
                address=user_address,
                total_bill=total_bill,
            )
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    item=item['item'],
                    price=item['item'].price,  
                    quantity=item['quantity']
                )

            cart.clear()

            return render(request, 'myaccount.html', {
                'order': order,
                'user': user,
                'order_records':order_records,
            })
    else:
        form = CheckOutForm(instance=user)

    return render(request,'buynow.html',{
            'cart':cart,
            'user':user,
            'form':form,
            'addresses': Address.objects.filter(user_profile=request.user)

    })

@login_required
def add_address(request):
    user = UserProfile.objects.get(user=request.user)
    order_records = Order.objects.filter(purchased_by=request.user)[:3]

    if request.method == 'POST':
        add_address_form = AddAddressForm(request.POST)
        if add_address_form.is_valid():
            address = add_address_form.save(commit=False)
            address.user_profile = request.user  # Associate the address with the user profile
            address.save()
            return render(request,'myaccount.html',{
                'user':user,
                'order_records':order_records,
                'addresses': Address.objects.filter(user_profile=request.user)
            })
        else:
            print("Form errors:", add_address_form.errors)
    else:
        add_address_form = AddAddressForm()

    return render(request, 'myaccount.html', {
        'add_address_form': add_address_form,
        'user': user,
        'order_records':order_records,
        'addresses': Address.objects.filter(user_profile=request.user)

    })

def order_history(request):
    order_records = Order.objects.filter(purchased_by=request.user)
    return render(request,'order_history.html',{
        'order_records':order_records,

    })

def order_details(request,order_id):
    # order_details=get_object_or_404(OrderItem,pk=order_id)
    order_details = OrderItem.objects.filter(order=order_id)

    print(order_details)
    return render(request,'order_details.html',{
        'order_details':order_details
    })