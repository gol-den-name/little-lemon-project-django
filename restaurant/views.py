from django.shortcuts import render
from .forms import bookingForm
from .models import booking, Menu


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about us", {})


def book(request):
    form = bookingForm()
    if request.method == "POST":
        form = bookingForm(request.POST)
        if form.is_valid():
            form.save()
        context = {"form": form}
        return render(request, "book.html", context)


def menu(request):
    menu_data = Menu.objects.all()
    return render(request, "menu.html", {"menu_data": menu_data})
