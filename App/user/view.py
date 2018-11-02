from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework import status, viewsets

from App.image.model import Image
from App.image.serializer import ImageSerializer
from App.rate.model import Rate
from App.rate.serializer import RateSerializer
from App.user.serializer import UserSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from App.code.view import (
    ForgotPasswordView,
    ValidateUserView
)


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
            status=status.HTTP_400_BAD_REQUEST
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

    def get_user_by_username(self, requeset, username):
        user = get_object_or_404(User, username=username)
        user_serializer = UserSerializer(user)
        return Response(
            user_serializer.data,
            status=status.HTTP_200_OK
        )

    def delete_user_by_username(self, request, username):
        # TODO - Verify permissions
        user = get_object_or_404(User, username=username)
        user.delete()
        return Response(
            'User delete',
            status=status.HTTP_200_OK
        )

    def update_user_by_username(self, request, username):
        # TODO - Verify permissions
        user = get_object_or_404(User, username=username)
        user_serializer = UserSerializer(data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.update(user, request.data)
        return Response(
            "User update",
            status=status.HTTP_200_OK
        )

    def get_activities_by_username(self, request, username):
        # TODO - not relation activity with user
        pass

    def get_image_by_username(self, request, username):
        image = Image.objects.get(user=username)
        image_serializer = ImageSerializer(image)
        return Response(
            image_serializer.data,
            status=status.HTTP_200_OK
        )

    def get_rate_by_username(self, request, username):
        user = get_object_or_404(User, username=username)
        average_rate = Rate.objects.filter(user_id=user.id).aggregate(Avg(
            "points"))
        return Response(
            average_rate,
            status.HTTP_200_OK
        )

    def post_rate_by_username(self, request, username):
        # TODO - Equal a create in view rate
        user = get_object_or_404(User, username=username)
        request.data['user_id'] = user.id
        rate_serializer = RateSerializer(data=request.data)
        rate_serializer.is_valid(raise_exception=True)
        rate_serializer.create(request.data)
        return Response(
            rate_serializer.data,
            status=status.HTTP_201_CREATED
        )

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


user = UserViewSet.as_view(dict(
    post='create',
    get='get_all_user'
))
user_by_username = UserViewSet.as_view(dict(
    get='get_user_by_username',
    put='update_user_by_username',
    delete='delete_user_by_username'
))

activities_by_username = UserViewSet.as_view(dict(
    get='get_activites_by_username'
))

images_by_username = UserViewSet.as_view(dict(
    get='get_image_by_username'
))

rates_by_username = UserViewSet.as_view(dict(
    get='get_rate_by_username',
    post='post_rate_by_username'
))

forgot_password = ForgotPasswordView.as_view(dict(
    get='get',
    post='post'
))

validate_user = ValidateUserView.as_view(dict(
    get='get'
))
