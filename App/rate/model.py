from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User


class Rate(models.Model):
    """

        This class represents the table Rate that is in the database. In the
        app users can receive a rate by other users for them to have a
        reputation so this class represents that rate.

    """
    points = models.FloatField(validators=[MinLengthValidator(0.0),
                                           MaxValueValidator(5.0)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO - add activity_id when the module is ready.
