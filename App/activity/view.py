from rest_framework import viewsets, status
from rest_framework.response import Response

from App.activity.serializer import ActivitySerializer


class ActivityView(viewsets.ViewSet):
    def create(self, request):
        activity_serializer = ActivitySerializer(data=request.data)
        if activity_serializer.is_valid():
            activity_serializer.create(request.data)
            return Response(
                activity_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            activity_serializer.errors,
            status=status.HTTP_200_OK
        )
