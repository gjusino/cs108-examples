from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from .models import *
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse

class AstronautView(ListView):
    """Create a subclass of Listview to display all heroes"""

    model = Astronaut
    template_name = 'project/all_astronauts.html'
    context_object_name = 'all_astronauts_list'


class AstronautPageView(DetailView):
    """Show us details for one hero"""
    model = Astronaut
    template_name = 'project/active_astronaut.html'
    context_object_name = 'hero'

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the hero record for this page view
        context = super(AstronautPageView, self).get_context_data(**kwargs)
        # create a new CreateCryforHelpForm, and add it into the context dictionary
        form = CreateSendMessageForm()
        context['create_send_message_form'] = form
        # return this context dictionary
        return context


class CrewView(ListView):
    """Show us list of teams"""

    model = Crew
    template_name= 'project/all_crews.html'
    context_object_name = 'all_crews_list'

class CrewPageView(DetailView):
    """Show us details of one team"""

    model = Crew
    template_name = 'project/crew.html'
    context_object_name = 'crew'


class CreateAstronautView(CreateView):
    """A view to create a new hero and save
    it to the database"""

    form_class = CreateAstronautForm
    template_name = 'project/create_astronaut.html'


class UpdateAstronautView(UpdateView):
    """A view to update a hero and save
    it to the database"""

    form_class = UpdateAstronautForm
    template_name = 'project/update_astronaut.html'
    queryset = Astronaut.objects.all()


class CreateCrewView(CreateView):
    """A view to create a new super team"""

    form_class = CreateCrewForm
    template_name= 'project/create_crew.html'


class UpdateCrewView(UpdateView):
    """A view to update a team and save
    it to the database"""

    form_class = UpdateCrewForm
    template_name = 'project/update_crew.html'
    queryset = Crew.objects.all()


class DeleteAstronautView(DeleteView):
    """A view to delete a hero and remove
    it from the database"""

    template_name = 'project/delete_astronaut.html'
    queryset = Astronaut.objects.all()
    success_url = '../../'

class DeleteCrewView(DeleteView):
    """A view to delete a team and remove
    it from the database"""

    template_name = 'project/delete_crew.html'
    queryset = Crew.objects.all()
    success_url = '../../crews'


def create_sendmessage(request, pk):
    '''
    Process a form submission to post a cry for help.
    '''
    # find the hero that matches the `pk` in the URL
    astro = Astronaut.objects.get(pk=pk)
    form = CreateSendMessageForm(request.POST or None, request.FILES or None)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']

        # save the new cry for help object to the database
        if form.is_valid():
            sm = form.save(commit=False)
            sm.astro = astro
            sm.save()
        else:
            print("Error: This form is not valid my guy")


    # redirect the user to the hero_page view
    return redirect(reverse('astronaut_page', kwargs={'pk': pk}))


class ShowMessagesViews(DetailView):
    """Shows the cries for help for every hero"""
    template_name = 'project/show_messages.html'
    model = Astronaut
    context_object_name = 'astronaut'


class HomePageView(TemplateView):
    """A specialized version of templateview
    to display our home page"""

    template_name = 'project/home.html'


class DeleteSendMessageView(DeleteView):
    """A view to resolve cries for help"""
    template_name = 'project/delete_messages.html'
    queryset= SendMessage.objects.all()
    
    def get_context_data(self,**kwargs):

        # Obtain default context data dictionary
        # by calling the super class version
        # of get_context_data and save it as context
        context = super(DeleteSendMessageView, self).get_context_data(**kwargs)
        st_cfh = SendMessage.objects.get(pk=self.kwargs['message_pk'])
        context['st_cfh']=st_cfh
        return context

    def get_object(self):
        """Return the cry for help that should be deleted"""
        # read the URL data values into variables
        astronaut_pk = self.kwargs['astronaut_pk']
        message_pk = self.kwargs['message_pk']

        # find the CryforHelp object, and return it
        st_cfh = SendMessage.objects.get(pk=message_pk)
        return st_cfh

    def get_success_url(self):
        """Returns the url to which to redirect the user"""
        astronaut_pk = self.kwargs['astronaut_pk']
        message_pk = self.kwargs['message_pk']
        k = reverse('astronaut_page',kwargs={"pk":astronaut_pk})
        return k