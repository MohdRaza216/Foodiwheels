from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

# Create your views here.

def get_random_image_url(query):
    api_key = 'XQcgcs3qRhQR1Z5W038M8eorJmAU2dbZ1k3kJG0OGKmVyydtEk0uHE1U'
    url = f'https://api.pexels.com/v1/search?query={query}&per_page=1'
    headers = {
        'Authorization': api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['photos']:
            image_url = data['photos'][0]['src']['original']
            return image_url
        else:
            return None
    else:
        return None
    
def index(request):
    query = 'water'
    image_url = get_random_image_url(query)
    return render(request, 'index.html', {'image_url': image_url})
 #   return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def veg(request):
    return render(request, 'veg.html')

def nonveg(request):
    return render(request, 'nonveg.html')

def login(request):
    return render(request, 'login.html')