from django.contrib import admin
from App.user.model import Profile
from App.image.model import Image
#from App.activity.model import Activity

admin.site.register(Profile)
#admin.site.register(Activity)
admin.site.register(Image)
