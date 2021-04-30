from django.db import models

# Create your models here.

from django.urls import reverse

# Create your models here.

class Astronaut(models.Model):
    """Encapsulate the idea of an Astronaut"""

    name= models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    hometown = models.TextField(blank=True)
    crew = models.ForeignKey('Crew', on_delete=models.CASCADE)
   
    def __str__(self):
        """return a string of this"""
        return '%s' %self.name

    def get_absolute_url(self):
        """Return a URL to display Hero"""
        return reverse("all_astronauts")
        #kwargs={"pk":self.pk})
    
    def get_message(self):
        """Gets the cries for help of all heroes"""
        message = SendMessage.objects.all().order_by("-timestamp")
        return message

class Crew(models.Model):
    """Encapsulate the idea of a superteam"""
    crew_name = models.TextField(blank=False)
    crew_image = models.URLField(blank=False)

    def __str__(self):
        """Return a string of this"""
        return self.crew_name

    def get_absolute_url(self):
        """Return a URL to display team"""
        return reverse('crew'), 
        #kwargs={"pk":self.pk})

    def get_all_heros(self):
        """Return all heroes"""
        astro = Astronaut.objects.filter(team=self.pk)
        return astro

class SendMessage(models.Model):
    """Model data attributes so heroes can post a cry for help"""

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    message = models.TextField(blank=True)
    astro = models.ForeignKey('Astronaut', on_delete=models.CASCADE)
    location = models.CharField(blank=False, max_length=25)

    def __str__(self):
        """Return a string representation
        of this object"""
        return '%s,%s' %(self.message, self.timestamp)