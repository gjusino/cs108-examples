from django import forms
from .models import *

class CreateProfileForm(forms.ModelForm):
    """Create a new profile"""

    class Meta:
        """Associate this to Profile"""
        model = Profile
        fields = ['first_name','last_name','city','profile_image_url',]

