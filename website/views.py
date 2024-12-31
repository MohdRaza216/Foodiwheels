from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FoodItem, Category
from .models import Message, Profile
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfileForm, UserForm, MessageForm
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.
def index(request):
    food_items = FoodItem.objects.select_related('category').all()
    return render(request, 'index.html', {'food_items': food_items})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

FOOD_ITEMS_TEMPLATE = 'food_items.html'

def veg(request):
    try:
        veg_category = Category.objects.get(name='Veg')
    except Category.DoesNotExist:
        return HttpResponse("Veg category not found.", status=404)
    food_items = FoodItem.objects.filter(category=veg_category)
    return render(request, FOOD_ITEMS_TEMPLATE, {'food_items': food_items, 'category': "Veg"})


def nonveg(request):
    try:
        non_veg_category = Category.objects.get(name='Non-Veg')
    except Category.DoesNotExist:
        return HttpResponse("Non-Veg category not found.", status=404)
    food_items = FoodItem.objects.filter(category=non_veg_category)
    return render(request, FOOD_ITEMS_TEMPLATE, {'food_items': food_items, 'category': "Non-Veg"})



def food_items_by_category(request, is_veg):
    food_items = FoodItem.objects.filter(category__is_veg=is_veg)
    return render(request, 'food_items.html', {
        'food_items': food_items,
        'category': "Veg" if is_veg else "Non-Veg",
    })


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('signup')

    return render(request, 'signup.html')

def login_view(request):
    next_url = request.GET.get('next', '/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect(next_url)
        messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

@login_required
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})

def profile_list(request):
    profiles = Profile.objects.all()  # Get all profiles from the database
    return render(request, 'profile_list.html', {'profiles': profiles})

def profile_update(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile_list')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'profile.html', context)

def submit_contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
        else:
            return render(request, 'contact.html', {"form": form})
    return redirect('contact')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def thank_you(request):
    return render(request, 'thank_you.html')
