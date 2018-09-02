#   from django.shortcuts import render
from App.user.view import UserViewSet

user = UserViewSet.as_view(dict(post='create'))
