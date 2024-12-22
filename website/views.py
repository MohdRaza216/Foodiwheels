from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from decouple import config
from .models import FoodItem, Category

# Create your views here.
def index(request):
    food_items = FoodItem.objects.all()
    return render(request, 'index.html', {'food_items': food_items})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def veg(request):
    veg_category = Category.objects.get(name='Veg')
    food_items = FoodItem.objects.filter(category=veg_category)
    return render(request, 'veg.html', {'food_items': food_items})

def nonveg(request):
    nonveg_category = Category.objects.get(name='Non-Veg')
    food_items = FoodItem.objects.filter(category=nonveg_category)
    return render(request, 'nonveg.html', {'food_items': food_items})


def login(request):
    return render(request, 'login.html')