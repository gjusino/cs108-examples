from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Astronaut)
admin.site.register(Crew)
admin.site.register(SendMessage)