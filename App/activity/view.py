import datetime

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from App.activity.model import Activity, ActivityUser
from App.activity.serializer import ActivitySerializer
from App.comment.view import CommentViewSet
from App.image.view import ImageViewSet
from .constants import ActivityQuerys


class ActivityView(viewsets.ViewSet):
    @staticmethod
    def create(request):
        request.data['user'] = request.user.id
        activity_serializer = ActivitySerializer(data=request.data)
        if activity_serializer.is_valid():
            activity_serializer.create(request.data)
            return Response("Ok",
                            status=status.HTTP_201_CREATED)
        return Response(activity_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def activity_list(request):
        if request.method == 'GET':
            activities = Activity.objects.raw(
                ActivityQuerys.get_query_activity_list(request.user.id)
            )
            activity_serializer = ActivitySerializer(
                activities,
                many=True,
            )
            return Response(activity_serializer.data,
                            status=status.HTTP_202_ACCEPTED)

    @staticmethod
    def activity_exact(request, pk):
        try:
            activity = Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            activity_serializer = ActivitySerializer(activity)
            return Response(activity_serializer.data,
                            status=status.HTTP_202_ACCEPTED)

        elif request.method == 'POST':
            ActivityUser.objects.create(
                user=request.user.id,
                activity=activity.id,
                rol=1
            )
            return Response("Register in the activity",
                            status=status.HTTP_202_ACCEPTED)

        elif request.method == 'PUT':
            get_object_or_404(
                ActivityUser,
                activity_id=activity.id,
                user_id=request.user.id
            )
            activity_serializer = ActivitySerializer(activity,
                                                     data=request.data)
            if activity_serializer.is_valid():
                activity_serializer.save()
                return Response(activity_serializer.data,
                                status=status.HTTP_202_ACCEPTED)
            return Response(activity_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            get_object_or_404(
                ActivityUser,
                activity_id=activity.id,
                user_id=request.user.id
            )
            activity.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get_activities_by_username(self, request, username):
        user = get_object_or_404(User, username=username)
        activities = Activity.objects.raw(
            ActivityQuerys.get_query_activity_list_by_user(
                user.id
            )
        )
        activity_serializer = ActivitySerializer(
            activities,
            many=True,
        )
        return Response(activity_serializer.data,
                        status=status.HTTP_202_ACCEPTED)

    def get_activities_by_username_own(self, request, username):
        user = get_object_or_404(User, username=username)
        activities = Activity.objects.raw(
            ActivityQuerys.get_query_activity_list_by_user_own(
                user.id
            )
        )
        activity_serializer = ActivitySerializer(
            activities,
            many=True,
        )
        return Response(activity_serializer.data,
                        status=status.HTTP_202_ACCEPTED)


activity_exact = ActivityView.as_view(dict(get='activity_exact',
                                           put='activity_exact',
                                           delete='activity_exact'))
activity = ActivityView.as_view(dict(post='create', get='activity_list'))
image_activity = ImageViewSet.as_view(dict(
    put='put_activity_image'
))

comments_by_activity = CommentViewSet.as_view(dict(
    post='post_comments_by_activity',
    get='get_comments_by_activity'
))
