from django.urls import path
from . import view

handler404 = 'views.page_not_found'

urlpatterns = (
    path(
        'comments/<int:comment_id>',
        view.comments_by_comment,
        name='comments_by_comment'
    ),
)
