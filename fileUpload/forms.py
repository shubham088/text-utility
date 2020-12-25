from django import forms
from .models import ImageCollections


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = ImageCollections
        fields = ('category', 'img', 'description')