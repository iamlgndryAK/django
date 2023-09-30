from django.shortcuts import render
from .models import Image
from .form import ImageForm


def home(request):
    if request.method == "POST":
        data = ImageForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
    form = ImageForm
    image = Image.objects.all()
    return render(request, "imager.html", context={'form': form, 'image': image})

