from django.urls import path, include
from . import view

handler404 = 'views.page_not_found'


urlpatterns = (
    path('activities/', view.activity, name='activity'),
    path('activities/<int:pk>', view.activity_exact, name='activity_pk'),
    path(
        'activities/<int:activity_id>/image',
        view.image_activity,
        name='image_activity'
    )
)
