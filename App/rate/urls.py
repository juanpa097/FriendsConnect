from django.urls import path
from . import view


handler404 = 'views.page_not_found'

urlpatterns = [
    path('rate/', view.rate, name='rate'),
    path('rate/<int:user_id>', view.rate_single, name='rate_id'),
]
