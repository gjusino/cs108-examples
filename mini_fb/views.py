from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CreateProfileForm
from django.shortcuts import redirect
from django.urls import reverse

class ShowAllProfilesView(ListView):
    '''Shows a listing of Profiles'''
    model = Profile #retrieve Profile objects from the database
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"

class ShowProfilePageView(DetailView):
    """Shows only one profile"""
    model= Profile
    template_name= 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'



class CreateProfileView(CreateView):
    """A view to Create a profile and 
    save it to the database"""
    form_class = CreateProfileForm

    template_name = 'mini_fb/create_profile_form.html'
