from django.urls import path
from .views import home, date, event, calculator
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", home, name="home"),
    path("<int:year>/<str:month>", date, name="date"),
    path("date/", date, name="date"),
    path("event/", event, name="event"),
    path("calculator/", calculator, name="calculator")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
