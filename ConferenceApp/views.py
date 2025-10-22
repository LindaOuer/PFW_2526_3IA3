from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
# Create your views here.

class ConferenceCreateView(CreateView):
    model = Conference
    fields = "__all__"
    template_name = 'conference/conference_form.html'
class ConferenceDetailsView(DetailView):
    model = Conference
    template_name = 'conference/conference_details.html'

def welcome(request):
    return HttpResponse("<h2>Welcome to the Conference App!</h2>")

def home(request, name):
    return render(request, 'conference/home.html', {'name': name})

# Afficher la liste des conf. à partir de la DB
def listConferences(request):
    conferences = Conference.objects.all()
    return render(
        request, 
        'conference/list_conferences.html',{'confs': conferences}
        )
    
class ConferenceListView(ListView):
    model = Conference
    template_name = 'conference/list_conferences.html'
    context_object_name = 'confs'