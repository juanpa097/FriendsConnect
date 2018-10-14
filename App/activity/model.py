from django.contrib.auth.models import User
from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    due_date = models.DateTimeField()
    max_participants = models.IntegerField()
    visibility = models.BooleanField()
    user_activity_id = models.ForeignKey(User, on_delete=models.CASCADE)
