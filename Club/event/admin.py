from django.contrib import admin
from .models import Person, Location, Event


admin.site.register(Person)
admin.site.register(Location)
admin.site.register(Event)
