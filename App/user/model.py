from django.db import models
from django.contrib.auth.models import User
from App.image.model import Image


class UserModel(models.Model):

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rol = models.IntegerField()
    about_me = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO Check if changue default, how to make the relation, if defalt photo
    #  image = models.OneToOneField(
    #   default=1, to=Image)
