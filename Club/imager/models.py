from django.db import models


class Image(models.Model):
    photo = models.ImageField(upload_to="assets")
    date = models.DateField(auto_now_add=True)
