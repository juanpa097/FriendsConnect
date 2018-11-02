from django.db import models
from django.contrib.auth.models import User


class CodeValidate(models.Model):
    user = models.OneToOneField(
        User,
        related_name='user_code',
        on_delete=models.PROTECT
    )
    code = models.CharField(
        max_length=6,
    )

    def __str__(self):
        return "Code: {}, with user: {}".format(
            self.code,
            self.user.username
        )
