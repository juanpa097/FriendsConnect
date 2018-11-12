from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .serializer import ForgotPasswordSerializer
from .mixins import (
    CodeGenMixin,
    ValidationCode
)


class ForgotPasswordView(
    viewsets.ViewSet,
    CodeGenMixin
):
    permission_classes = (AllowAny,)

    def post(self, request, email):
        request.data['email'] = email
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(request.data)
        return Response('OK')

    def get(self, request: object, email: object) -> object:
        user = get_object_or_404(User, email=email)
        self.generate_password_reset_code(user)
        return Response('OK')


class ValidateUserView(
    viewsets.ViewSet,
    ValidationCode,
    CodeGenMixin
):
    def get(self, request: object, username: object, code: object) -> object:
        self.validate_code(username, code)
        return Response('OK')

    def resend_email(self, request, username):
        user = get_object_or_404(User, username=username)
        self.generate_user_validate_code(user)
        return Response('OK')
