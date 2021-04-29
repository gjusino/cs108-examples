from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    """Create a new profile"""

    class Meta:
        """Associate this to Profile"""
        model = Profile
        fields = ['first_name','last_name','city','profile_image_url',]

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile 
        fields = ['city', 'email_address','profile_image_url']

class CreateStatusMessageForm(forms.ModelForm):
     image = forms.ImageField(required=False)
     
     class Meta:
        model = StatusMessage
        fields = ['message', 'image']