from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rol = models.IntegerField()
    about_me = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
