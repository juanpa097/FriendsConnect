#   from django.shortcuts import render
from App.user.view import UserViewSet
from App.auth.view import ObtainExpiringAuthToken

user = UserViewSet.as_view(dict(post='create'))
auth = ObtainExpiringAuthToken.as_view()
