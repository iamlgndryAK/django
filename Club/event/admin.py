from django.contrib import admin
from .models import Person
from .models import Location
from .models import Event


admin.site.register(Person)
admin.site.register(Location)
admin.site.register(Event)
