from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
    path('user/', views.user),
    path('login/', views.auth),
    path('image/', views.image),
    path('image/<int:id>/', views.image),
]
