from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),  # This matches {% url 'home' %}
    path("book/", views.book, name="book"),  # This matches {% url 'book' %}
]
