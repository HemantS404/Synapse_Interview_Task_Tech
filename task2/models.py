from django.db import models

class EventManagment(models.Model):
    name = models.CharField(max_length=100)
    date_of_event = models.DateTimeField()
    event_complete = models.BooleanField()
    No_of_audience = models.IntegerField()
    Email_of_organizer = models.EmailField(default='admin@gmail.com')

    def __str__(self):
        return self.name