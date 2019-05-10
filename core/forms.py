from django import forms
from core.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'