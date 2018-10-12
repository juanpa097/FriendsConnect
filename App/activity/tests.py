from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .model import Activity
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from datetime import datetime


class ActivityTests(APITestCase):
    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email,
                                             self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def test_create_Activity(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('activity')
        data = {
            "name": "testAc",
            "description": "Des...",
            "location": "111",
            "due_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "max_participants": 3,
            "visibility": "True"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)

    def test_get_Activities(self):
        """
        Get more than one item if get all activities
        """
        url = reverse('activity')
        data = {
            "name": "testAc",
            "description": "Des...",
            "location": "111",
            "due_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "max_participants": 3,
            "visibility": "True"
        }
        self.client.post(url, data, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(len(response.data), 1)

    def test_create_Activity_date_less_now(self):
        """
                Ensure we can create a new account object.
                """
        url = reverse('activity')
        data = {
            "name": "testAc",
            "description": "Des...",
            "location": "111",
            "due_date": "2010-10-12 23:06:42",
            "max_participants": 3,
            "visibility": "True"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Activity.objects.count(), 0)

    def test_create_Activity_max_participant_negative(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('activity')
        data = {
            "name": "testAc",
            "description": "Des...",
            "location": "111",
            "due_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "max_participants": -1,
            "visibility": "True"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Activity.objects.count(), 0)

    def test_get_activity(self):
        url = reverse('activity')
        data = {
            "name": "testAc",
            "description": "Des...",
            "location": "111",
            "due_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "max_participants": 5,
            "visibility": "True"
        }
        self.client.post(url, data, format='json')
        url = reverse('activity_pk', args=(1,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['name'], "testAc")

    def test_put_activity(self):
        url = reverse('activity')
        data = {
            "name": "testAc",
            "description": "Des...",
            "location": "111",
            "due_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "max_participants": 5,
            "visibility": "True"
        }
        self.client.post(url, data, format='json')
        url = reverse('activity_pk', args=(1,))
        data['name'] = "test2"
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['name'], "test2")

    def test_delete_activity(self):
        url = reverse('activity')
        data = {
            "name": "testAc",
            "description": "Des...",
            "location": "111",
            "due_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "max_participants": 5,
            "visibility": "True"
        }
        self.client.post(url, data, format='json')
        url = reverse('activity_pk', args=(1,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Activity.objects.count(), 0)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
