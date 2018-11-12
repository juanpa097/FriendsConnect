from django.contrib import admin

from App.activity.model import Activity
from App.user.model import Profile
from App.image.model import Image
from App.code.model import CodeValidate
from App.activity.model import ActivityUser
from App.comment.model import Comment

admin.site.register(Profile)
admin.site.register(Activity)
admin.site.register(Image)
admin.site.register(CodeValidate)
admin.site.register(ActivityUser)
admin.site.register(Comment)
