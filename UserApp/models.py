from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.

name_validator = RegexValidator(
    regex=r'^[a-zA-Z]+$',
    message="This field should contain only alphabetic characters."
)

def validate_email(value):
    allowed_domains = ['esprit.tn', 'univ.tn', 'mit.edu', 'ox.ac.uk']
    domain = value.split("@")[-1]
    if domain not in allowed_domains:
        raise ValidationError(f"Email domain must be one of the following: {', '.join(allowed_domains)}")
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Participant', 'Participant'),
        ('Committee', 'Committee'),
    ]
    
    first_name = models.CharField(max_length=30, validators=[name_validator])
    last_name = models.CharField(max_length=30, validators=[name_validator])
    email = models.EmailField(unique=True, validators=[validate_email])
    affiliation = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Participant')
    nationality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)