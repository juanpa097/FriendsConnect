import base64
import os
from random import randint

from django.core.files.base import ContentFile

from FriendsConnect.settings import MEDIA_ROOT


class CreateImageBy64Mixin:
    random_image = 0

    def getFileBy64(self, image):
        return ContentFile(base64.b64decode(image), name='temp')
        '''
        self.set_random()
        path = MEDIA_ROOT + '/' +self.random_image
        with open(path, "wb+") as image_file:
            image_in_str = base64.b64decode(str(image))
            image_file.write(image_in_str)
        return image_file
        '''

    def deleteImage(self):
        path = MEDIA_ROOT + '/' + self.random_image
        os.remove(path)

    def set_random(self):
        self.random_image = str(
            randint(
                0,
                999999
            )
        )