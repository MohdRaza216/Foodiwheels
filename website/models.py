from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    name = models.CharField(max_length=100, blank=True, default="Default Name")
    phone = models.CharField(max_length=15, blank=True, default="0000000000")
    desc = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name or 'Unknown'}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_veg = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        
class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="food_items")
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField( max_length=500, blank=True)
    phone = models.CharField(max_length=15, blank=True, default="0000000000")
    address = models.TextField(blank=True, default="No address provided")
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default_profile.png', blank=True, null=True)

    def __str__(self):
        return self.user.username


    def __str__(self):
        return self.user.username
