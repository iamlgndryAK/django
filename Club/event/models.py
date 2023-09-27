from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    web = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.location_name}"


class Person(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Event(models.Model):

    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    person = models.ManyToManyField(Person, blank=True)

    def __str__(self):
        return f"{self.event_name}"


