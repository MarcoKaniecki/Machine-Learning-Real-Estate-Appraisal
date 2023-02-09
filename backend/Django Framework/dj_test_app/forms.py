from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AlbumForm(forms.ModelForm):
    name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    
    class Meta:
        model = ImageAlbum
        fields = ('name', 'description')
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name == "":
            cleaned_data['name'] = "Default Name"
        
        if description == "":
            cleaned_data['description'] = "Default Description"