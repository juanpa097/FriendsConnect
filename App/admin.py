from django.contrib import admin

from App.activity.model import Activity
from App.user.model import Profile
from App.image.model import Image


admin.site.register(Profile)
admin.site.register(Activity)
admin.site.register(Image)
