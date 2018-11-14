from django.urls import path
from . import view


handler404 = 'views.page_not_found'

urlpatterns = [
    path('images/', view.image, name='image'),
    path('images/<int:id>', view.image),
]
