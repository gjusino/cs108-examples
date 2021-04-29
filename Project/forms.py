# This is my form page. This includes forms in order to create Heroes, Teams, and a cry for help 
# we can also update heroes and teams. 

from django import forms
from .models import * 


class CreateAstronautForm(forms.ModelForm):
    """A form to add new heros"""

    class Meta:
        """Associate this with hero model"""
        model = Astronaut
        fields = ['name','image_url','hometown','crew']


class UpdateAstronautForm(forms.ModelForm):
    """A form to update a hero"""

    class Meta:
        """Associate this with hero model"""
        model = Astronaut
        fields = ['name','image_url','crew']


class CreateCrewForm(forms.ModelForm):
    """A form to add new heros"""

    class Meta:
        """Associate this with team model"""
        model = Crew
        fields = ['crew_name','crew_image']

class UpdateCrewForm(forms.ModelForm):
    """A form to update a Team"""

    class Meta:
        """Associate this with team model"""
        model = Crew
        fields = ['crew_name','crew_image']

class CreateSendMessageForm(forms.ModelForm):
    """A form to create a cry for help"""

    class Meta:
        """Associate this to CryforHelp"""
        model = SendMessage
        fields = ['message','location']