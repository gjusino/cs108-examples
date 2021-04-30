# urls for everything in my project. There is a comment next to each about what they do.

from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),   # shows home page
    path('astronaut',AstronautView.as_view(), name='all_astronauts'),   # shows all heroes
   # path('astronaut/', AstronautPageView.as_view(),name='astronaut_page'),   # a heros page
    path('crew/<int:pk>', CrewPageView.as_view(),name='crew_page'),   # shows a team page

    path('crews',CrewView.as_view(), name='crew'),   # shows all teams 
    path('create_astronaut',CreateAstronautView.as_view(),name='create_astronaut'),  # register a hero
    path('astronaut/<int:pk>/update', UpdateAstronautView.as_view(),name='update_astronaut'),   # update an existing hero
   # path('create_team',CreateCrewView.as_view(),name='create_crew'),   # register a team
    path('crew/<int:pk>/update', UpdateCrewView.as_view(),name='update_crew'),    # update an existing team
    path('astronaut/<int:pk>/delete', DeleteAstronautView.as_view(),name='delete_astronaut'),    # delete a hero
    path('crew/<int:pk>/delete', DeleteCrewView.as_view(),name='delete_crew'),    # delete a team
    path('astronaut/<int:pk>/post_message',create_sendmessage, name='post_message'),          # post a cry for help 
    path('astronaut/<int:pk>/show_cries',ShowMessagesViews.as_view(),name='show_message'),     # shows the cries from heroes
    path('astronaut/<int:astronaut_pk>/delete_sendmessage/<int:message_pk>', DeleteSendMessageView.as_view(), name="delete_sendmessage"), # resolve a cry for help
]