#   from django.shortcuts import render

from App.activity.view import ActivityView
from App.user.view import UserViewSet
from App.auth.view import ObtainExpiringAuthToken

user = UserViewSet.as_view(dict(post='create', get='get_all_user'))
auth = ObtainExpiringAuthToken.as_view()
activity = ActivityView.as_view({'get': 'activity_exact', 'put': 'activity_exact', 'delete': 'activity_exact'})
activity2 = ActivityView.as_view({'post': 'create', 'get': 'activity_list'})

