from django.contrib.auth.models import User
from rest_framework import status, viewsets
from App.user.serializer import UserSerializer, UserModelSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


from App.user.model import UserModel


class UserViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.create(request.data)
            return Response(
                user_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            user_serializer.errors,
            status=status.HTTP_200_OK
        )

    # Retrives all user from de db
    def get_all_user(self, request):
        all_user = User.objects.all()

        users_serializer = UserSerializer(
            all_user,
            many=True
        )
        return Response(
            users_serializer.data,
            status=status.HTTP_200_OK
        )

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
