from django.db import models
from Apps.universities.models import University
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200, null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)
    startDate = models.DateTimeField('date started', null=True, blank=True)
    endDate = models.DateTimeField('date ended', null=True, blank=True)
    university = models.ForeignKey(University, related_name='eventList', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.text

