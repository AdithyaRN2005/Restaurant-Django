from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('menu/',views.menu, name='menu'),
    path('signup/', views.signup, name = 'signup'),
    path('myaccount/', views.myaccount, name = 'myaccount'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
    path('change-quantity/<str:product_id>/',views.change_quantity, name='change_quantity'),
    path('remove-from-cart/<str:product_id>/',views.remove_from_cart, name='remove_from_cart'),
    path('<slug:slug>/',views.category_detail, name='category_detail'),


]

