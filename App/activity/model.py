from django.contrib.auth.models import User
from django.db import models
from App.image.model import Image


class Activity(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    due_date = models.DateTimeField()
    max_participants = models.IntegerField()
    visibility = models.BooleanField()
    users = models.ManyToManyField(
        User,
        related_name='activities',
        through='ActivityUser',
    )
    # TODO Check if changue default, how to make the relation, if defalt photo
    image = models.OneToOneField(
        null=True,
        to=Image,
        on_delete=models.CASCADE
    )


class ActivityUser(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO - missings constants
    rol = models.IntegerField(default=1)
