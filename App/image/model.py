from django.db import models
from FriendsConnect.settings import MEDIA_ROOT
from django.contrib.auth.models import User
import os


def directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    path = MEDIA_ROOT + f'/Images/' \
                        f'_{instance.id}'
    return path


class Image(models.Model):
    file = models.FileField(blank=False, null=False,
                            upload_to=directory_path)

    def delete(self, *args, **kwargs):
        os.remove(self.file.path)
        super(Image, self).delete(*args, **kwargs)
