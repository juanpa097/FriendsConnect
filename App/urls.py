from django.urls import path, include
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
    path('user/', views.user),
    path('login/', views.auth),
    path('', include('App.rate.urls'))
]
