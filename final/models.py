from django.db import models

# Create your models here.

class Astronaut(model.Models):
    '''represents an astronaut'''

    name = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    hometown = models.TextField(blank=True)
    messages_from_earth = models.

    def __str__(self):
        """return a string of this"""
        return '%s' %self.name