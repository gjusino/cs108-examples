# mini_fb/admin.py
from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import StatusMessage
admin.site.register(Profile)
admin.site.register(StatusMessage)