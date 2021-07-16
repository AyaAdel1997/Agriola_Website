from django import forms
from .models import Imagemodel

class ImageForm(forms.ModelForm):
    class Meta:
        model= Imagemodel
        fields=('images',)

"""class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
"""