from django.urls import path
from website import views
from . import views
from django.shortcuts import render

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("veg", views.veg, name="veg"),
    path("nonveg", views.nonveg, name="nonveg"),
    path("login", views.login, name="login"),
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
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

]

