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
        """Return a URL to display Astronaut"""
        return reverse("astronaut_page", kwargs={"pk":self.pk})
    
    def get_message(self):
        """Gets the messages of all Astronauts"""
        messages = SendMessage.objects.all().order_by("-timestamp")
        return messages

class Crew(models.Model):
    """Encapsulate the idea of a crew"""
    crew_name = models.TextField(blank=False)
    crew_image = models.URLField(blank=False)

    def __str__(self):
        """Return a string of this"""
        return self.crew_name

    def get_absolute_url(self):
        """Return a URL to display crew"""
        return reverse('crew_page',kwargs ={"pk":self.pk})

    def get_all_astronauts(self):
        """Return all astronauts"""
        astronauts = Astronaut.objects.filter(crew=self.pk)
        return astronauts

class SendMessage(models.Model):
    """Model data attributes so people can send messages"""

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    message = models.TextField(blank=True)
    astronaut = models.ForeignKey('Astronaut', on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation
        of this object"""
        return '%s,%s' %(self.message, self.timestamp)
        