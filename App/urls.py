from django.urls import path, include


handler404 = 'views.page_not_found'

urlpatterns = [
    path('', include('App.user.urls')),
    path('', include('App.auth.urls')),
    path('', include('App.image.urls')),
]
