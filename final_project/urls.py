# urls for everything in my project

from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),   # shows home page
    path('astronaut',AstronautView.as_view(), name='all_astronauts'),   # shows all astronauts
    path('astronaut/<int:pk>', AstronautPageView.as_view(),name='astronaut_page'),   # an astronauts page
    path('crew/<int:pk>', CrewPageView.as_view(),name='crew_page'),   # shows a crew page
    path('crews',CrewView.as_view(), name='crew'),   # shows all crew 
    path('create_astronaut',CreateAstronautView.as_view(),name='create_astronaut'),  # register an astronaut
    path('astronaut/<int:pk>/update', UpdateAstronautView.as_view(),name='update_astronaut'),   # update an existing astronaut
    path('create_crew',CreateCrewView.as_view(),name='create_crew'),   # register a crew
    path('crew/<int:pk>/update', UpdateCrewView.as_view(),name='update_crew'),    # update an existing crew
    path('astronaut/<int:pk>/delete', DeleteAstronautView.as_view(),name='delete_astronaut'),    # delete an astronaut
    path('crew/<int:pk>/delete', DeleteCrewView.as_view(),name='delete_crew'),    # delete a crew
    path('astronaut/<int:pk>/post_message',create_sendmessage, name='post_message'),          # post a message 
    path('astronaut/<int:pk>/show_message',ShowMessagesViews.as_view(),name='show_message'),     # shows the messages
    path('astronaut/<int:astronaut_pk>/delete_sendmessage/<int:message_pk>', DeleteSendMessageView.as_view(), name="delete_sendmessage"), # resolve a sent message
]