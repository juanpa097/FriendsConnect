from django.core import mail
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from datetime import datetime
import datetime as date

from App.activity.model import Activity, ActivityUser
from App.code.model import CodeValidate
from App.rate.model import Rate
from App.activity.tests import ActivityTests


class UserTests(APITestCase):
    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email,
                                             self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def test_get_all_user(self):
        data = {
            "username": "testsUser",
            "password": "you_know:v",
        }
        User.objects.create(**data)
        url = reverse('users')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_user_by_username(self):
        data = {
            "username": "testsUser",
            "password": "you_know:v",
        }
        User.objects.create(**data)
        username = "testsUser"
        url = reverse('user_by_username', args=(username, ))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testsUser')

    def test_delete_user_by_username(self):
        data = {
            "username": "testsUser",
            "password": "you_know:v",
        }
        User.objects.create(**data)
        username = "testsUser"
        url = reverse('user_by_username', args=(username,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)

    def test_update_user_by_username(self):
        # TODO - Verify is update profile
        data = {
            "username": "testsUser",
            "password": "you_know:v",
            "email": "t@t.c"
        }
        User.objects.create(**data)
        username = "testsUser"
        url = reverse('user_by_username', args=(username,))
        data['first_name'] = 'Nnn'
        data.pop("username")
        data.pop("email")
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(username="testsUser")
        self.assertEqual(user.first_name, 'Nnn')

    def test_get_image_by_username(self):
        # TODO I don't know how make this
        pass

    def post_rate_by_username(self):
        data = {
            'points': 3.0
        }
        url = reverse('rates_by_username', args=(self.user.username,))
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Rate.objects.count(), 1)

    def test_get_rate_by_username(self):
        data = {
            'user_id': self.user,
            'points': 3.0
        }
        Rate.objects.create(**data)
        data['points'] = 4.0
        Rate.objects.create(**data)
        data['points'] = 5.0
        Rate.objects.create(**data)

        url = reverse('rates_by_username', args=(self.user.username,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['points__avg'], 4.0)

    def test_suscribe_activity(self):
        activity = Activity.objects.create(
            **ActivityTests._get_default_activity()
        )
        url = reverse(
            'user_and_activity_actions',
            args=(self.username, activity.id)
        )
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ActivityUser.objects.count(), 1)

    def test_suscribe_activity_full(self):
        activity = Activity.objects.create(
            **ActivityTests._get_default_activity(max_participants=1)
        )
        url = reverse(
            'user_and_activity_actions',
            args=(self.username, activity.id)
        )
        response = self.client.post(url, format='json')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unsuscribe_activity(self):
        activity = Activity.objects.create(
            **ActivityTests._get_default_activity()
        )
        ActivityUser.objects.create(
            user=self.user,
            activity=activity
        )
        url = reverse(
            'user_and_activity_actions',
            args=(self.username, activity.id)
        )
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ActivityUser.objects.count(), 0)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


class UserTestsNoCredentials(APITestCase):

    def test_create(self):
        """
                Ensure we can create a new account object.
        """
        url = reverse('users')
        data = {
            "username": "testsUser",
            "password": "you_know:v",
            "email": "test@test.com",
            "profile": {
                "about_me": "--"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(CodeValidate.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Welcome to Friends Connect!')
