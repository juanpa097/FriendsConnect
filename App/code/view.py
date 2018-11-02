from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from App.code.constants import EmailTemplates
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
        reset_password_constant = EmailTemplates.get_reset_password()
        template_data = serializer.validated_data
        # TODO - Send email
        return Response('OK')

    def get(self, request, email):
        user = get_object_or_404(User, email=email)
        self.generate_password_reset_code(user)
        # TODO - Send email
        return Response('OK')

class ValidateUserView(
    viewsets.ViewSet,
    ValidationCode
):
    def get(self, request, username, code):
        self.validate_code(username, code)
        return Response('OK')