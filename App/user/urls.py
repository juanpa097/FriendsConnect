from . import view
from django.urls import path, include

handler404 = 'views.page_not_found'

urlpatterns = [

    path('users/', view.user, name='users'),
    path('users/<slug:username>', view.user_by_username,
         name='user_by_username'),
    path(
        'users/<slug:username>/activities',
        view.activities_by_username,
        name='activities_by_username'
    ),
    path(
        'users/<slug:username>/rates',
        view.rates_by_username,
        name='rates_by_username'
    ),
    path(
        'users/<slug:username>/validate/<slug:code>',
        view.validate_user,
        name='validate_user'
    ),
    path(
        'users/<slug:username>/image',
        view.image_user,
        name='image_user'
    ),
    path(
        'users/<str:email>/reset_password',
        view.forgot_password,
        name='reset_password_user'
    ),
]
