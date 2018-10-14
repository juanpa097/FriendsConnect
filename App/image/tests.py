from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .model import Image
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
        url = reverse('image')
        data = {'file': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Image.objects.count(), 0)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
