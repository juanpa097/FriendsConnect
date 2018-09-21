import django.urls

from App.activity.view import ActivityView

handler404 = 'views.page_not_found'

urlpatterns = [
    django.urls.path('activity/', ActivityView.as_view(dict(post='create', get='activity_list'))),
    django.urls.path('activity/<int:pk>', ActivityView.as_view(dict(get='activity_exact', put='activity_exact', delete='activity_exact')))
]

### activity_exact = ActivityView.as_view(dict(get='activity_exact', put='activity_exact', delete='activity_exact'))
### activity = ActivityView.as_view(dict(post='create', get='activity_list'))