from django.db import models

# The models file in Django defines the database schema for the application, including the tables, fields, and relationships between them. 
# It also provides an object-relational mapping (ORM) layer for interacting with the database, 
# allowing developers to work with Python objects instead of writing raw SQL queries.

class Post(models.Model):
    # content is a paragraph description of the house (will change in the future)
    zone = models.CharField(max_length=100, blank=True, null=True)
    lotArea = models.IntegerField(blank=True, null=True)
    
    image = models.ImageField(upload_to='post_images')
    
    def __str__(self):
        return self.title