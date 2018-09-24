from django.urls import path, include
from . import view

handler404 = 'views.page_not_found'


urlpatterns = (
    path('activity/', view.activity),
    path('activity/<int:pk>', view.activity_exact)
)