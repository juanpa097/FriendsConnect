from django.urls import path, include
from . import view


handler404 = 'views.page_not_found'

urlpatterns = [
    path('user/', view.user),
]
