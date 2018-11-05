from django.contrib import admin

from App.activity.model import Activity
from App.user.model import Profile
from App.image.model import Image
from App.code.model import CodeValidate


admin.site.register(Profile)
admin.site.register(Activity)
admin.site.register(Image)
admin.site.register(CodeValidate)
