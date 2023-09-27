from django.shortcuts import render
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
