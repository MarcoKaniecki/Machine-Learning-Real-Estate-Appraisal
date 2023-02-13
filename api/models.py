from django.db import models

# Create your models here.



'''
class Listing(models.Model):
    address = models.CharField(max_length=255)
    
class Image(models.Model):
    image = models.ImageField(upload_to='')
    # title = models.CharField(max_length=255, default='Default title')
    # description = models.CharField(max_length=255, default='Default description')
    # default = models.BooleanField(default=False)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE, default=0)
'''