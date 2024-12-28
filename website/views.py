from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FoodItem, Category
from .models import Message, Profile
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfileForm

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


def food_items_by_category(request, is_veg):
    food_items = FoodItem.objects.filter(category__is_veg=is_veg)
    context = {
        'food_items': food_items,
        'category': "Veg" if is_veg else "Non-Veg",
    }
    return render(request, 'food_items.html', context)

def submit_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("message")

        # Validate the phone number (10-12 digits)
        if not re.match(r'^\d{10,12}$', phone):
            return HttpResponse("Invalid phone number. Please enter a valid 10-12 digit number.")

        # Save the message to the database
        Message.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc
        )

        # Redirect to the thank you page
        return redirect("thank_you")

    return HttpResponse("Invalid request.")


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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

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