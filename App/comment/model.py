from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from App.activity.model import Activity


class Comment(models.Model):
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField(
        auto_now_add=True, blank=True
    )
    # TODO - verify on delete
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment',
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name='comment',
        blank=True,
        null=True
    )
    replies = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='comment',
        null=True,
        blank=True
    )
