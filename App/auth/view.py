from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny

from datetime import datetime


class ObtainExpiringAuthToken(ObtainAuthToken):

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(
                user=user
            )

            if not created:
                token.created = datetime.utcnow()
                token.save()
            response_data = {
                'token': token.key,
                'validate': user.profile.rol != -1
            }
            return Response(
                response_data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request):
        token = get_object_or_404(Token, user=request.user)
        token.delete()
        return Response(
            "OK",
            status=status.HTTP_200_OK
        )

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


auth = ObtainExpiringAuthToken.as_view()
