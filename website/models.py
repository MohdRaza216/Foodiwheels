from django.db import models

# Create your models here.
class Message (models.Model):
    name = models.CharField(max_length=200),
    email = models.CharField(max_length=100),
    phone = models.CharField(max_length=12),
    desc = models.TextField(max_length=10000, blank =True),

