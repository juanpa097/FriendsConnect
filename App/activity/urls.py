from django.urls import path, include
from . import view

handler404 = 'views.page_not_found'


urlpatterns = (
    path('activities/', view.activity, name='activity'),
    path('activity/<int:pk>', view.activity_exact, name='activity_pk')
)
