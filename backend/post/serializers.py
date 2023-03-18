from rest_framework import serializers
from .models import *

# shortcut for creating serializers that deal with model instances and querysets.
# Automatically generate fields based on the model fields and provide default implementations for creating or updating instances.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=False)
    # images = ImageSerializer(many=True)

    class Meta:
        model = Listing
        fields = '__all__'
 

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        # Debugging messages
        if len(images_data):
            print('Not empty')
        else:
            print('Empty')
        listing = Listing.objects.create(**validated_data)
        for image_data in images_data:
            Image.objects.create(listing=listing, image=image_data)
        return listing
    
    # def create(self, validated_data):
    #     images_data = validated_data.pop('images')
    #     listing = Listing.objects.create(**validated_data)
    #     for image_data in images_data:
    #         Image.objects.create(listing=listing, **image_data)
    #     return listing