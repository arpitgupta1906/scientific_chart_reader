from django import forms
from .models import IMAGE


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=IMAGE
        fields=['data']
