from rest_framework import viewsets, status
from rest_framework.response import Response

from App.activity.model import Activity
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

    ##  @api_view(['GET', 'POST'])
    def Activity_list(self, request):
        if request.method == 'GET':
            activities = Activity.objects.all()
            activity_serializer = ActivitySerializer(activities, many=True)
            return Response(activity_serializer.data)

    ##  @api_view(['GET', 'PUT', 'DELETE'])
    def activity_exact(request, pk):
        """
        Retrieve, update or delete a snippet instance.
        """

        try:
            activity = Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            activity_serializer = ActivitySerializer(activity)
            return Response(activity_serializer.data)

        elif request.method == 'PUT':
            activity_serializer = ActivitySerializer(activity, data=request.data)
            if activity_serializer.is_valid():
                activity_serializer.save()
                return Response(activity_serializer.data)
            return Response(activity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            activity.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
