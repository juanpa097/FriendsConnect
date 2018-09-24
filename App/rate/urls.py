from django.urls import path
from . import view


handler404 = 'views.page_not_found'

urlpatterns = [
    path('rate/', view.rate),
    path('image/<int:id>/', view.rate_single),
]
