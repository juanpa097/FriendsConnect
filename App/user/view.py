from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework import status, viewsets

from App.activity.model import Activity, ActivityUser
from App.activity.view import ActivityView
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
from App.image.view import ImageViewSet


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

    def suscribe_to_activity(self, request, username, activity_id):
        user, activity = self._get_user_and_activity(username, activity_id)
        if ActivityUser.objects.filter(user_id=user.id, id=activity_id).count() > 0:
            return Response(
                "Subscription already made",
                status=status.HTTP_400_BAD_REQUEST
            )

        participants = ActivityUser.objects.filter(
            activity_id=activity.id
        ).count()
        if participants >= activity.max_participants:
            return Response(
                "The activity is complete",
                status=status.HTTP_400_BAD_REQUEST
            )
        ActivityUser.objects.create(
            user=user,
            activity=activity
        )
        return Response(
            "OK",
            status=status.HTTP_200_OK
        )

    def unsuscribe_to_activity(self, request, username, activity_id):
        user, activity = self._get_user_and_activity(username, activity_id)
        relation = ActivityUser.objects.get(
            user=user,
            activity=activity
        )
        relation.delete()
        return Response(
            "OK",
            status=status.HTTP_200_OK
        )

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def _get_user_and_activity(self, username, activity_id):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {'username': "User not found"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            activity = Activity.objects.get(id=activity_id)
        except Activity.DoesNotExist:
            return Response(
                {'activity': "Activity not found"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return user, activity


user = UserViewSet.as_view(dict(
    post='create',
    get='get_all_user'
))
user_by_username = UserViewSet.as_view(dict(
    get='get_user_by_username',
    put='update_user_by_username',
    delete='delete_user_by_username'
))

activities_by_username = ActivityView.as_view(dict(
    get='get_activities_by_username'
))

activities_by_username_own = ActivityView.as_view(dict(
    get='get_activities_by_username_own'
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

image_user = ImageViewSet.as_view(dict(
    put='put_user_image',
    get='get_image_by_username'
))

user_and_activity_actions = UserViewSet.as_view(dict(
    post='suscribe_to_activity',
    delete='unsuscribe_to_activity'
))

validate_user_resend = ValidateUserView.as_view(dict(
    get='resend_email'
))
