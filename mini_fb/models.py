from django.db import models

# Create your models here.
class Profile(models.Model):
    '''represents profile created by new user'''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)

    def __str__(self):
        '''return a string representation of this object.'''
        
        
        return f'{self.first_name} {self.last_name}, {self.city}'

    def get_status_messages(self):
        """Gets the statuses of each profile"""
        status = StatusMessage.objects.filter(profile=self.pk)
        return status 

    def __str__(self):
        """Return a string representation
        of this object"""

        return '%s,%s' %(self.last_name, self.first_name)

    def get_absolute_url(self):
        """ Return a URL to display the new profile """
        return reverse("show_profile_page", kwargs={"pk":self.pk})


class StatusMessage(models.Model):
    """Model the data attributes of a Facebook
    status message"""

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    message =models.TextField(blank=True)
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        """Return a string representation
        of this object"""
        return '%s,%s' %(self.message, self.timestamp)

