from django.db import models

class Comment(models.Model):
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField()
# TO DO: PK, FK