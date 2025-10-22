
from django.urls import path
from . import views

urlpatterns = [
    path('home/<str:name>', views.home, name='home'),
    path('list/', views.listConferences, name='conference-list'),
    path('listC/', views.ConferenceListView.as_view(), name='conference-listLV'),
    path('welcome/', views.welcome, name='welcome'),
    path('details/<int:pk>/', views.ConferenceDetailsView.as_view(), name='conference-details'),
]
