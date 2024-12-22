from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    desc = models.TextField(max_length=10000, blank=True)


    def __str__(self):
        return f"Message from {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="food_items")
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)  

    def __str__(self):
        return self.name
