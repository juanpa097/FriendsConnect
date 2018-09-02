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

            token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])

            if not created:
                token.created = datetime.utcnow()
                token.save()
            response_data = {'token': token.key}
            return Response(
                response_data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]