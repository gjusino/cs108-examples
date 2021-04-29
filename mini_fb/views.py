from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from django.shortcuts import redirect
from django.urls import reverse

class ShowAllProfilesView(ListView):
    '''Shows a listing of Profiles'''
    model = Profile #retrieve Profile objects from the database
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"

class ShowProfilePageView(DetailView):
    """Shows only one profile"""
    model= Profile
    template_name= 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    """A view to Create a profile and 
    save it to the database"""
    form_class = CreateProfileForm

    template_name = 'mini_fb/create_profile_form.html'

class UpdateProfileView(UpdateView):

    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'
    
    def create_status_message(request, pk):
        '''Process a form submission to post a new status message.'''
    # find the profile that matches the `pk` in the URL
        profile = Profile.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
        if request.method == 'POST':

            # read the data from this form submission
            message = request.POST['message']

            # save the new status message object to the database
            if message:

                sm = StatusMessage()
                sm.profile = profile
                sm.message = message
                sm.image = image
                sm.save()

        # redirect the user to the show_profile_page view
        return redirect(reverse('show_profile_page', kwargs={'pk': pk}))

class DeleteStatusMessage(DetailView):
    
    template_name = 'mini_fb/delete_status_form.html'
    queryset = StatusMessage.objects.all()
    def get_context_data(self, **kwargs):
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['st_msg']= st_msg
        return context

class DeleteStatusView(DetailView):

    def get_object(self):
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # find the StatusMessage object, and return it
        return profile_pk, status_pk

    def get_success_url(self):
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']
        k = reverse('show_profile_page',kwargs={"pk":profile_pk})
        return k


class ShowNewsFeedView(DetailView):

    template_name = 'show_news_feed.html'
    model = Profile

class ShowPossibleFriendsView(DetailView):
    model = Profile
    template_name = 'possible_friends.html'
