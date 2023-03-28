from django.contrib import admin
from .models import *

# Register your models here.

# provides a web-based interface for managing the data stored in the app's models
# admin.site.register(Post)
admin.site.register(Listing)
admin.site.register(Image)