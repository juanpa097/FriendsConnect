from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    due_date = models.DateTimeField()
    max_participants = models.IntegerField()
    visibility = models.BooleanField()
    #User_Activity_id = models.IntegerField()
