from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

class ShowAllProfilesView(ListView):
    '''Shows a listing of Profiles'''
    model = Profile #retrieve Profile objects from the database
    template_name = "show_all_profiles.html"
    context_object_name = "profiles"