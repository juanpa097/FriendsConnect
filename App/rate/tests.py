from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .model import Rate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class ImageTests(APITestCase):
    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email,
                                             self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def test_create_Image(self):
        """
        Ensure we can't create a new account object.
        """
        url = reverse('rate')
        data = {
            'user_id': self.user.id,
            'points': 3.0
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rate.objects.count(), 1)

    def test_get_average_rate(self):
        data = {
            'user_id': self.user,
            'points': 3.0
        }
        Rate.objects.create(**data)
        data['points'] = 4.0
        Rate.objects.create(**data)
        data['points'] = 5.0
        Rate.objects.create(**data)

        url = reverse('rate_id', args=(self.user.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['points__avg'], 4.0)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
