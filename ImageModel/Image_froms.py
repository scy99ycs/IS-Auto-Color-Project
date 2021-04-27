from django import forms
from django.core.exceptions import ValidationError
from ImageModel import models

class image(forms.Form):
    name = forms.CharField(min_length=4)
    img = forms.ImageField(upload_to='style_img')