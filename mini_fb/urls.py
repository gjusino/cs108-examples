# file: mini_fb/urls.py
# description: direct url requests to view functions

from django.urls import path
from .views import *

urlpatterns = [
    path('home', ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>',ShowProfilePageView.as_view(),name='show_profile_page'),
    path('create_profile',CreateProfileView.as_view(), name='create_profile'),
    ]