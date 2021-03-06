from django.urls import path, include

handler404 = 'views.page_not_found'

urlpatterns = [
    path('', include('App.rate.urls')),
    path('', include('App.user.urls')),
    path('', include('App.auth.urls')),
    path('', include('App.image.urls')),
    path('', include('App.activity.urls')),
    path('', include('App.comment.urls')),
]
