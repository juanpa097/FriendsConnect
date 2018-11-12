from django.db import models
from django.contrib.auth.models import User
from App.image.model import Image


class Profile(models.Model):

    rol = models.IntegerField(default=-1)
    about_me = models.CharField(max_length=200)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    # TODO Check if changue default, how to make the relation, if defalt photo
    image = models.OneToOneField(
        null=True,
        to=Image,
        on_delete=models.CASCADE
    )
