from django.contrib import admin
from django.urls import path
from website import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('veg', views.veg, name='veg'),
    path('nonveg', views.nonveg, name='nonveg'),
    path('login', views.login, name='login'),
    path('food/veg/', views.food_items_by_category, {'is_veg': True}, name='food_veg'),
    path('food/nonveg/', views.food_items_by_category, {'is_veg': False}, name='food_nonveg'),
]

