from rest_framework import serializers
from .models import Post

# shortcut for creating serializers that deal with model instances and querysets.
# Automatically generate fields based on the model fields and provide default implementations for creating or updating instances.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
