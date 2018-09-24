from rest_framework import status, viewsets
from rest_framework.response import Response
from django.db.models import Avg
from .model import Rate
from .serializer import RateSerializer


class RateViewSet(viewsets.ViewSet):
    """

        This class contains the methods that are going to be called when
        the user makes a get request or any HTTP method.

    """

    def create(self, request):
        """
            Creates a new Rate using the information provided by the user.
            :type request: Request
            :rtype Response
        """
        rate_serializer = RateSerializer(data=request.data)
        if rate_serializer.is_valid():
            rate_serializer.create(request.data)
            return Response(
                rate_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            rate_serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )

    def get_all_rates(self, request):
        """
            Gets all rates
            :rtype: Response
        """
        rate_serializer = RateSerializer(
            Rate.objects.all(),
            many=True
        )

        return Response(
            rate_serializer.data,
            status=status.HTTP_200_OK
        )

    def get_average_rate(self, request, user_id):
        """
            Gets the average user's rate
            :param user_id: Int
            :rtype: Response
        """
        average_rate = Rate.objects.filter(user_id=user_id).aggregate(Avg(
            "points"))
        return Response(
            average_rate,
            status.HTTP_200_OK
        )


rate = RateViewSet.as_view(dict(
    post='create',
    get='get_all_rates'
))

rate_single = RateViewSet.as_view(dict(
    get='get_average_rate'
))
