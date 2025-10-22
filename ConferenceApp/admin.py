from django.contrib import admin
from .models import Conference, Submission, OrganizingCommittee

# Register your models here.
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme', 'location', 'start_date', 'end_date')
    list_filter = ('theme', 'location')
    search_fields = ('name', 'theme', 'location')
    ordering = ('-start_date',)

admin.site.register(Conference, ConferenceAdmin) 
admin.site.register(Submission) 
admin.site.register(OrganizingCommittee) 