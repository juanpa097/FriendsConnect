from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    due_date = models.DateTimeField()
    max_participants = models.IntegerField()
    visibility = models.BooleanField()
# User_Activity_id = models.ForeignKey('UserModel', on_delete=models.CASCADE)
