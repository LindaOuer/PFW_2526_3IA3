from django import forms
from .models import Conference


class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ["name", "theme", "location", "start_date", "end_date", "description"]
        widgets = {
            "start_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "end_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "description": forms.Textarea(attrs={"rows": 5, "class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "theme": forms.Select(attrs={"class": "form-select"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "name": "Nom de la Conférence",
            "theme": "Thème",
            "location": "Lieu",
            "start_date": "Date de Début",
            "end_date": "Date de Fin",
            "description": "Description (min. 30 caractères)",
        }

