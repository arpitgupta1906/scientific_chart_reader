from django import forms
from .models import IMAGE


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=IMAGE
        fields=['data']

        # widgets={
        #     'data':forms.ImageField(attrs={'class':'imageinputclass'}),
        # }

    def __init__(self, *args, **kwargs):
        super(ImageUploadForm, self).__init__(*args, **kwargs)
        self.fields['data'].widget.attrs.update({
            'class': 'imageclass'
        })