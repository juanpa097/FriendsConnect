from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .model import Image


class ImageTests(APITestCase):
    def test_create_Image(self):
        """
        Ensure we can't create a new account object.
        """
        url = reverse('imageAPI')
        data = {'file': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Image.objects.count(), 0)
