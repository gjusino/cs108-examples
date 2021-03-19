from django.shortcuts import render
from django.views.generic import ListView
from .models import Quote
# Create your views here.

class HomePageView(ListView):
    '''show a listing of Quotes.'''
    model = Quote # retireve Quote objects from the database
    template_name = "quotes/home.html"
    context_object_name = "quotes"