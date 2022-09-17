from django.contrib import admin
from task2.models import EventManagment

class EM(admin.ModelAdmin):
    list_display = ('name','date_of_event','event_complete','No_of_audience')

admin.site.register(EventManagment,EM)
