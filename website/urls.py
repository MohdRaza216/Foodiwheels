from django.urls import path
from website import views
from . import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .views import profile

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("veg", views.veg, name="veg"),
    path("nonveg", views.nonveg, name="nonveg"),
    path("food/veg/", views.food_items_by_category, {"is_veg": True}, name="food_veg"),
    path(
        "food/nonveg/",
        views.food_items_by_category,
        {"is_veg": False},
        name="food_nonveg",
    ),
    path("submit_contact/", views.submit_contact, name="submit_contact"),
    path(
        "thank_you/",
        lambda request: render(request, "thank_you.html"),
        name="thank_you",
    ),
    path("signup/", views.signup_view, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", views.logout_view, name="logout"),
    path(
        "password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path('profile/', profile, name='profile'),
    path('profiles/', views.profile_list, name='profile_list'),
]
