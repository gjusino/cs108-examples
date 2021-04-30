from django import forms
from .models import * 


class CreateAstronautForm(forms.ModelForm):
    """A form to add new astronauts"""

    class Meta:
        """Associate this with astronaut model"""
        model = Astronaut
        fields = ['name','image_url','hometown','crew']


class UpdateAstronautForm(forms.ModelForm):
    """A form to update an astronaut"""

    class Meta:
        """Associate this with astronaut model"""
        model = Astronaut
        fields = ['name','image_url','crew']


class CreateCrewForm(forms.ModelForm):
    """A form to add new crews"""

    class Meta:
        """Associate this with crew model"""
        model = Crew
        fields = ['crew_name','crew_image']

class UpdateCrewForm(forms.ModelForm):
    """A form to update a crew"""

    class Meta:
        """Associate this with crew model"""
        model = Crew
        fields = ['crew_name','crew_image']

class CreateSendMessageForm(forms.ModelForm):
    """A form to create a message"""

    class Meta:
        """Associate this to SendMessage"""
        model = SendMessage
        fields = ['message','location']