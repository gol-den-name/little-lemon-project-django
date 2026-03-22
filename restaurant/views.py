from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "welcome to little lemon", {})


def about(request):
    return render(request, "about us", {})


def book(request):
    return HttpResponse("This is the reservation page.")
