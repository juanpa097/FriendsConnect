from django.conf.urls import url
from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = {
    path('user/', views.user),
    path('login/', views.auth),
    path('activity/', views.activity),
    path(r'^activity/(?P<year>[0-9]{4})/$', views.activity, name='activity_exact'),
}


