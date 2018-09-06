from django.db import models


class Image(models.Model):

    image_base64 = models.CharField(max_length=50000)