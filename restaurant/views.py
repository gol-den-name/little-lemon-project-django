from django.shortcuts import render
from .forms import BookingForm
from .models import booking, Menu


def index(request):
    return render(request, "restaurant/index.html")


def about(request):
    return render(request, "about us", {})


def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "restaurant/book.html", context)


def menu(request):
    menu_data = Menu.objects.all()
    return render(request, "menu.html", {"menu_data": menu_data})
