# file: mini_fb/urls.py
# description: direct url requests to view functions

from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    #path('profile/<int:pk>/post_status', create_status_message.as_view(), name='post_status'),
    #path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name='delete_status'),
    #path('profile/<int:profile_pk>/news_feed', ShowNewsFeedView.as_view(), name='news_feed'),
    #path('profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name='show_possible_friends'),
    #path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', ShowPossibleFriendsView.as_view(), name='add_friend'),
]