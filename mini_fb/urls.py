# file: mini_fb/urls.py
# description: direct url requests to view functions

from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>',ShowProfilePageView.as_view(),name='show_profile_page'),
]