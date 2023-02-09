from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from DjangoTesting import settings
from .forms import *
import os


# Create your views here.
def say_hello(request):
    return render(request, 'hello.html')

def success(request):
    return render(request, 'success.html')

def display_images(request):
 
    if request.method == 'GET':
        Albums = ImageAlbum.objects.all()
        Images = Image.objects.all()
        return render(request, 'images.html', {'album_list': Albums,'image_list': Images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def upload_album(request):
    if request.method == 'POST':
        
        album_name = request.POST.get('name')
        album_description = request.POST.get('description')
        a = ImageAlbum(name = album_name,description = album_description)
        a.save()
        images = request.FILES.getlist('images')
        for image in images:
            b = Image(image = image,album = a)
            b.save()

    return render(request, 'upload.html')

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('display')

def delete_album(request, album_id):
    album = get_object_or_404(ImageAlbum, id=album_id)
    album.delete()
    return redirect('display')