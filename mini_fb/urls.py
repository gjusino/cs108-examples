# file: mini_fb/urls.py
# description: direct url requests to view functions

from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),

]