from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
<<<<<<< HEAD
    django.urls.path('user/', views.user),
    django.urls.path('login/', views.auth),
    django.urls.path('activity/', views.activity),
    django.urls.path('activity/<int:pk>', views.activity_exact)
=======
    path('user/', views.user),
    path('login/', views.auth),
    path('activity/', views.activity),
    path('activity/<int:id>/', views.activity)
>>>>>>> parent of 8e60259... Activity v2.0
]
