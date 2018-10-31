from django.urls import path, include
from . import view

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
        'users/<slug:username>/images',
        view.images_by_username,
        name='images_by_username'
    ),
    path(
        'users/<slug:username>/rates',
        view.rates_by_username,
        name='rates_by_username'
    ),

]
