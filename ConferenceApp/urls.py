
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.listConferences, name='conference-list'),
    path('listC/', views.ConferenceListView.as_view(), name='conference-listLV'),
]
