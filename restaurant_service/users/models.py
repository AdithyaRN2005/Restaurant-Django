from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)


    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
    

DRAFT = 'draft'
ACTIVE = 'active'
DELETED = 'deleted'
NOT_AVAILABLE = 'not_available'

STATUS_CHOICES = (
(DRAFT, 'draft'),
(ACTIVE, 'active'),
(DELETED, 'deleted'),
(NOT_AVAILABLE,'not_available'),

)


class Item(models.Model):
    category = models.ManyToManyField(Category, related_name='Items')
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50) 
    image = models.ImageField(upload_to='uploads/item images', blank=True, null=True)

    description = models.TextField(blank=True)
    price = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default=ACTIVE)

    def __str__(self):
        return self.title
    


HOME = 'home'
WORK = 'work'
OTHERS = 'others'

TYPE_CHOICES = (
    (HOME,'home'),
    (WORK,'work'),
    (OTHERS,'others'),
)

class Address(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50, choices=TYPE_CHOICES,default=HOME)
    housename = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    postoffice = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    mob = models.IntegerField()
    
    def __str__(self):
        return f"{self.name}, {self.housename},{self.place}"


class Order(models.Model):
    item = models.ManyToManyField(Item,related_name='orders')
    total_bill = models.IntegerField()
    purchased_by = models.ForeignKey(User, related_name='orders',on_delete=models.SET_NULL,blank=True, null=True)
    purchased_at = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address,on_delete=models.DO_NOTHING,blank=True, null=True)
    email = models.EmailField(null=True)
    
    class Meta:
        ordering = ['-purchased_at']
        
    def __str__(self):
        return f"Order #{self.id}"

    def calculate_total_bill(self):
        self.total_bill = sum(order_item.item.price * order_item.quantity for order_item in self.orderitem_set.all())
        self.save()
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_display_price(self):
        return self.price