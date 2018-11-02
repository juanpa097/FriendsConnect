from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from App.image.model import Image
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
import datetime as date
from App.activity.model import Activity


class ImageTests(APITestCase):
    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email,
                                             self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.path = 'App/image/tests/img.png'

    def test_create_Image_wron_message(self):
        """
        Ensure we can't create a new account object.
        """
        url = reverse('image')
        data = {'file': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Image.objects.count(), 0)

    def test_create_Image(self):
        """
        Ensure we can create a new image object.
        """
        url = reverse('image')

        image = SimpleUploadedFile(
            self.path,
            b"file_content"
        )
        response = self.client.post(url, {'file': image})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.count(), 1)

    def test_put_user_Image(self):
        """
        Ensure we can update a new image object.
        """
        url = reverse('image_user', args=(self.username,))
        image = SimpleUploadedFile(
            self.path,
            b"file_content"
        )
        response = self.client.put(url, {'file': image})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Image.objects.count(), 1)

    def test_put_activity_Image(self):
        """
        Ensure we can update a new image object.
        """

        activity = self._create_activity()
        url = reverse('image_activity', args=(activity.id,))
        image = SimpleUploadedFile(
            self.path,
            b"file_content"
        )
        response = self.client.put(url, {'file': image})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Image.objects.count(), 1)

    def _create_activity(self):
        time = datetime.now()
        time += date.timedelta(days=10)
        data = {
            "name": "testAc",
            "description": "Des...",
            "location": "111",
            "due_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "max_participants": 3,
            "visibility": "True",
        }
        return Activity.objects.create(**data)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
