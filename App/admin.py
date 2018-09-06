from django.contrib import admin
from App.user.model import UserModel
from App.image.model import Image

admin.site.register(UserModel)
admin.site.register(Image)