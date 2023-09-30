from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from calendar import HTMLCalendar, month_name
from .models import Event
from datetime import datetime

now = datetime.now()


def home(request):
    return render(request, "home.html", context={})


def date(request, year=now.year, month=now.strftime('%B')):
    month = month.capitalize()
    month_number = list(month_name).index(month)
    calendar_data = HTMLCalendar().formatmonth(year, month_number)
    return render(request, "date.html", context={"year": year,
                                                 "month": month,
                                                 "day": now.date().day,
                                                 "calendar_data": calendar_data})


def event(request):
    event_list = Event.objects.all()
    return render(request, "event.html", context={"event_list": event_list})


def calculator(request):
    return render(request, "calculator.html")


def form(request):
    return render(request, "form.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, "home.html")
        else:
            messages.success(request, "Invalid username or password!!")
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def admin_login(request):
    return redirect('/admin/')
