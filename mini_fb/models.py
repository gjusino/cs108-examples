from django.db import models
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    '''represents profile created by new user'''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank= True)
    email_address = models.TextField(blank= True)
    profile_image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")

    def get_friend_suggestions(self):
        possible_friends = Profile.objects.filter(profile_is = 'get_friends')
        return possible_friends

    def get_news_feed(self):
        """Return the news feed items"""
        news1 = StatusMessage.objects.filter(profile__in = self.get_friends()).order_by("-timestamp")
        news2 = StatusMessage.objects.filter(profile=self.pk).order_by("-timestamp")
        news3 = news1 | news2
        return news3

    def get_friends(self):
        queryset = friends.objects.all()
        return queryset


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
        return '%s,%s' % (self.message, self.timestamp, self.profile)