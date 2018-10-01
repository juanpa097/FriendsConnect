from django.db import models
from datetime import datetime

class Comment(models.Model):
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField(default=datetime.now())
    user =
# TO DO: PK, FK