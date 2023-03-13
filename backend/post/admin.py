from django.contrib import admin
from .models import Post

# Register your models here.

# provides a web-based interface for managing the data stored in the app's models
admin.site.register(Post)
