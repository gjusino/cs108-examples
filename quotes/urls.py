# quotes/urls.py

from django.urls import path
from .views import HomePageView # our view class definition

urlpatterns = [
    path('',HomePageView.as_view(), name="home_page"),
    
]