from django import forms
from Image_file_App.models import UploadedImage

class UploadedImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = '__all__'