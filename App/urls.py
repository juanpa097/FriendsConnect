import django.urls
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
    django.urls.path('user/', views.user),
    django.urls.path('login/', views.auth),
    django.urls.path('activity/', views.activity),
    django.urls.path('activity/<int:pk>', views.activity_exact)
]
