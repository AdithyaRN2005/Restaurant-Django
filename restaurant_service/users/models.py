from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

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