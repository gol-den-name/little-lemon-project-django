from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),  # {% url 'home' %}
    path("book/", views.book, name="book"),  # {% url 'book' %}
    path("menu/", views.menu, name="menu"),  # {% url 'menu' %}
]
