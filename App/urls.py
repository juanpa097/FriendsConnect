from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
    path('user/', views.user),
]
