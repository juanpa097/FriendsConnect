from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    due_date = models.DateTimeField()
    max_participants = models.IntegerField()
    visibility = models.BooleanField()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    # User_Activity_id = models.IntegerField()
=======
    #User_Activity_id = models.IntegerField()
>>>>>>> parent of 83bee6f... Activity v3.0 cascade
=======
    #User_Activity_id = models.IntegerField()
>>>>>>> parent of 83bee6f... Activity v3.0 cascade
=======
    #User_Activity_id = models.IntegerField()
>>>>>>> parent of 83bee6f... Activity v3.0 cascade
