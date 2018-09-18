from rest_framework import viewsets, status
from rest_framework.response import Response

from App.activity.model import Activity
from App.activity.serializer import ActivitySerializer


class ActivityView(viewsets.ViewSet):
    @staticmethod
    def create(request):
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

    @staticmethod
    def activity_list(request):
        if request.method == 'GET':
            activities = Activity.objects.all()
            activity_serializer = ActivitySerializer(activities, many=True)
            return Response(activity_serializer.data)

    @staticmethod
    def activity_exact(request, pk):
        try:
            print("pipiLoco was hereeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            activity = Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            print("GET pipiLoco was hereeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            activity_serializer = ActivitySerializer(activity)
            return Response(activity_serializer.data)

        elif request.method == 'PUT':
            print("PUT pipiLoco was hereeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            activity_serializer = ActivitySerializer(activity, data=request.data)
            if activity_serializer.is_valid():
                activity_serializer.save()
                return Response(activity_serializer.data)
            return Response(activity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            print("DELETE pipiLoco was hereeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            activity.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
