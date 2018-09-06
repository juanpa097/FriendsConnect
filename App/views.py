#   from django.shortcuts import render
from App.user.view import UserViewSet
from App.auth.view import ObtainExpiringAuthToken
from App.image.view import ImageViewSet

user = UserViewSet.as_view(dict(
    post='create',
    get='get_all_user'
))
auth = ObtainExpiringAuthToken.as_view()
image = ImageViewSet.as_view(dict(
    post='create'
))
