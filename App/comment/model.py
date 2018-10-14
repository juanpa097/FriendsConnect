from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Comment(models.Model):
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='comment'
    )
    replies = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='comment',
        null=True
    )
