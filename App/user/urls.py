from django.urls import path, include
from . import view

handler404 = 'views.page_not_found'

urlpatterns = [
    path('users/', view.user, name='users'),
    path('user/<slug:username>', view.user_by_username,
         name='user_by_username'),
    path(
        'user/<slug:username>/activities',
        view.activities_by_username,
        name='activities_by_username'
    ),
    path(
        'user/<slug:username>/images',
        view.images_by_username,
        name='images_by_username'
    ),
    path(
        'user/<slug:username>/rates',
        view.rates_by_username,
        name='rates_by_username'
    ),

]
