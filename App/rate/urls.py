from django.urls import path
from . import view


handler404 = 'views.page_not_found'

urlpatterns = [
    path('rates/', view.rate, name='rate'),
    path('rates/<int:user_id>', view.rate_single, name='rate_id'),
]
