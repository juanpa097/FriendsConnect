from django.urls import path
from . import view


handler404 = 'views.page_not_found'

urlpatterns = [
    path('image/', view.image, name='image'),
    path('image/<int:id>/', view.image),
]
