from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from datetime import datetime

from App.rate.model import Rate
from App.code.model import CodeValidate


class ForgotPasswordTests(APITestCase):
    def setUp(self):
        self.data = {
            "username": "testsUser",
            "password": "you_know:v",
            "email": "test@test.com"
        }
        self.user = User.objects.create(**self.data)

    def test_get_forgot_password(self):
        email = self.user.email
        url = reverse('reset_password_user', args=(email, ))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(CodeValidate.objects.all()), 1)

    def test_wrong_email_forgot_password(self):
        data = self.data
        data['username'] = 'test2'
        data['email'] = 'test2@test.com'
        otherUser = User.objects.create(**self.data)
        email = otherUser.email
        code = "000000"
        code = CodeValidate.objects.create(code=code, user=self.user)
        json = {
            "code": code.code,
            "password": "test123"
        }
        url = reverse('reset_password_user', args=(email,))
        response = self.client.post(url,json, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(set(response.data), {'ErrorCode'})

    def test_post_forgot_password(self):
        code = "000000"
        code = CodeValidate.objects.create(code=code, user=self.user)
        json = {
            "code": code.code,
            "password": "test123"
        }
        email = self.user.email
        url = reverse('reset_password_user', args=(email,))
        response = self.client.post(url, json, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(username=self.user.username)
        self.assertNotEqual(self.user.password, user.password)

class ValidateCodeUserTest(APITestCase):
    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email,
                                             self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def test_validate_user_code(self):
        code = "000000"
        code = CodeValidate.objects.create(code=code, user=self.user)
        url = reverse('validate_user', args=(self.username,code.code))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "OK")

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
