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
        

