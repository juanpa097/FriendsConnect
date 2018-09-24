from django.contrib import admin

from App.activity.model import Activity
from App.user.model import UserModel


admin.site.register(UserModel)
admin.site.register(Activity)
