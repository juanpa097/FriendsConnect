from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from App.activity.model import Activity
from App.activity.tests import ActivityTests
from App.comment.model import Comment


class CommentTests(APITestCase):
    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email,
                                             self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_comments_by_comment(self):
        comment = self._get_default_comment("NOT")
        comment = Comment.objects.create(**comment)
        comment2 = self._get_default_comment("NN")
        comment2['replies'] = comment
        Comment.objects.create(**comment2)
        url = reverse('comments_by_comment', args=(comment.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_post_comments_by_comment(self):
        comment = self._get_default_comment("NOT")
        comment = Comment.objects.create(**comment)
        comment2 = self._get_default_comment("NN", user=1)
        url = reverse('comments_by_comment', args=(comment.id,))
        response = self.client.post(url, comment2, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.all().count(), 2)

    def test_get_comments_by_activity(self):
        activity = ActivityTests._get_default_activity()
        activity = Activity.objects.create(**activity)
        comment = self._get_default_comment("NOT")
        comment['activity'] = activity
        comment = Comment.objects.create(**comment)
        url = reverse('comments_by_activity', args=(activity.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_post_comments_by_activity(self):
        activity = ActivityTests._get_default_activity()
        activity = Activity.objects.create(**activity)
        comment = self._get_default_comment("NOT", user=1)
        url = reverse('comments_by_activity', args=(activity.id,))
        response = self.client.post(url, comment, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.all().count(), 1)

    def _get_default_comment(
            self,
            description,
            user=None
    ):
        if not user:
            user = self.user
        comment = {
            'description': description,
            'user': user
        }
        return comment
