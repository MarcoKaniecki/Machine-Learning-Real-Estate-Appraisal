from django.db import models
from DjangoTesting import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

# Create your models here.
class ImageAlbum(models.Model):
    name = models.CharField(max_length=255, default='Default album name')
    description = models.CharField(max_length=255, default='Default description')
    def default(self):
        return self.images.filter(default=True).first()

class Listing(models.Model):
    address = models.CharField(max_length=255)
    #album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE, default='None')

class Image(models.Model):
    image = models.ImageField(upload_to='')
    # title = models.CharField(max_length=255, default='Default title')
    # description = models.CharField(max_length=255, default='Default description')
    # default = models.BooleanField(default=False)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE, default=0)

@receiver(post_delete, sender=Image)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)