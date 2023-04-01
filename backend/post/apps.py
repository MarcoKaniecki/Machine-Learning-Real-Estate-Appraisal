from django.apps import AppConfig

# The apps file in Django is used to organize related code into reusable components that can be plugged into different projects. 
# It defines the configuration for the app, including the database settings, URL routing, and any dependencies on other apps.

class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
