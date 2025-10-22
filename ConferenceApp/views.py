from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse("<h2>Welcome to the Conference App!</h2>")





def home(request):
    return render(request, 'conference/home.html')



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