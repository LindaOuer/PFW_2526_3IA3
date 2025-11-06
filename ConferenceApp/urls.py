from django.urls import path
from . import views

urlpatterns = [
    path("home/<str:name>", views.home, name="home"),
    path("list/", views.listConferences, name="conference-list"),
    path("listC/", views.ConferenceListView.as_view(), name="conference-listLV"),
    path("welcome/", views.welcome, name="welcome"),
    path(
        "details/<int:pk>/",
        views.ConferenceDetailsView.as_view(),
        name="conference_details",
    ),
    path("create/", views.ConferenceCreateView.as_view(), name="conference_create"),
    path(
        "update/<int:pk>/",
        views.ConferenceUpdateView.as_view(),
        name="conference_update",
    ),
    path(
        "delete/<int:pk>/",
        views.ConferenceDeleteView.as_view(),
        name="conference_delete",
    ),
]
