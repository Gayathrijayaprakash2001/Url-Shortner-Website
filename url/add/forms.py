# forms.py

from django import forms
from .models import UrlModel  # make sure UrlModel is your correct model name

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlModel
        fields = ['title', 'original_url']  # Use your model field names
