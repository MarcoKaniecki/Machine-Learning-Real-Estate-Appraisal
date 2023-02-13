from django.db import models

# Create your models here.

'''
class Appraisal(models.Model):
    # currently set that its not required to have an image
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.CharField(max_length=1000)
    
    def __str__(self):
        # representation when used from admin panel
        # only return a portion of the data since it may be very long
        return self.images[0:2], self.description[0:50]
'''