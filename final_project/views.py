from django.shortcuts import render

# Create your views here.
from .models import *
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse

class AstronautView(ListView):
    """Create a subclass of Listview to display all astronauts"""

    model = Astronaut
    template_name = 'final_project/all_astronauts.html'
    context_object_name = 'all_astronauts_list'


class AstronautPageView(DetailView):
    """Show us details for one astronaut"""
    model = Astronaut
    template_name = 'final_project/astronaut.html'
    context_object_name = 'astronaut'

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the astronaut record for this page view
        context = super(AstronautPageView, self).get_context_data(**kwargs)
        # create a new CreateSendMessageForm, and add it into the context dictionary
        form = CreateSendMessageForm()
        context['create_send_message_form'] = form
        # return this context dictionary
        return context


class CrewView(ListView):
    """Show us list of crews"""

    model = Crew
    template_name= 'final_project/all_crews.html'
    context_object_name = 'all_crews_list'

class CrewPageView(DetailView):
    """Show us details of one crew"""

    model = Crew
    template_name = 'final_project/crew.html'
    context_object_name = 'crew'


class CreateAstronautView(CreateView):
    """A view to create a new astronaut and saves
    it to the database"""

    form_class = CreateAstronautForm
    template_name = 'final_project/create_astronaut.html'


class UpdateAstronautView(UpdateView):
    """A view to update an astronaut and save
    it to the database"""

    form_class = UpdateAstronautForm
    template_name = 'final_project/update_astronaut.html'
    queryset = Astronaut.objects.all()


class CreateCrewView(CreateView):
    """A view to create a new crew"""

    form_class = CreateCrewForm
    template_name= 'final_project/create_crew.html'


class UpdateCrewView(UpdateView):
    """A view to update a crew and save
    it to the database"""

    form_class = UpdateCrewForm
    template_name = 'final_project/update_crew.html'
    queryset = Crew.objects.all()


class DeleteAstronautView(DeleteView):
    """A view to delete an astronaut and remove
    it from the database"""

    template_name = 'final_project/delete_astronaut.html'
    queryset = Astronaut.objects.all()
    success_url = '../../astronaut'

class DeleteCrewView(DeleteView):
    """A view to delete a crew and remove
    it from the database"""

    template_name = 'final_project/delete_crew.html'
    queryset = Crew.objects.all()
    success_url = '../../crews'


def create_sendmessage(request, pk):
    '''
    Process a form submission to post a message.
    '''
    # find the astronaut that matches the `pk` in the URL
    astro = Astronaut.objects.get(pk=pk)
    form = CreateSendMessageForm(request.POST or None, request.FILES or None)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']

        # save the new message object to the database
        if form.is_valid():
            formMessage = form.save(commit=False)
            formMessage.astronaut = astro
            formMessage.save()
        else:
            print("Error: This form is not valid")


    # redirect the user to the astronaut_page view
    return redirect(reverse('astronaut_page', kwargs={'pk': pk}))


class ShowMessagesViews(DetailView):
    """Shows the messages for every astronaut"""
    template_name = 'final_project/show_message.html'
    model = Astronaut
    context_object_name = 'astronaut'


class HomePageView(TemplateView):
    """A specialized version of templateview
    to display our home page"""

    template_name = 'final_project/home.html'


class DeleteSendMessageView(DeleteView):
    """A view to resolve recieved messages"""
    template_name = 'final_project/delete_message.html'
    queryset= SendMessage.objects.all()
    
    def get_context_data(self,**kwargs):

        # Obtain default context data dictionary
        # by calling the super class version
        # of get_context_data and save it as context
        context = super(DeleteSendMessageView, self).get_context_data(**kwargs)
        st_sm = SendMessage.objects.get(pk=self.kwargs['message_pk'])
        context['st_sm']=st_sm
        return context

    def get_object(self):
        """Return the message that should be deleted"""
        # read the URL data values into variables
        astronaut_pk = self.kwargs['astronaut_pk']
        message_pk = self.kwargs['message_pk']

        # find the SendMessage object, and return it
        st_cfh = SendMessage.objects.get(pk=message_pk)
        return st_cfh

    def get_success_url(self):
        """Returns the url to which to redirect the user"""
        astronaut_pk = self.kwargs['astronaut_pk']
        message_pk = self.kwargs['message_pk']
        k = reverse('show_message',kwargs={"pk":astronaut_pk})
        return k