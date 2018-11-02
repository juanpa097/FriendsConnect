from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from App.activity.model import Activity
from App.image.model import Image
from App.image.serializer import ImageSerializer


class ImageViewSet(viewsets.ViewSet):

    def create(self, request):
        image_serializer = ImageSerializer(data=request.data)
        image_serializer.is_valid(raise_exception=True)
        image_serializer.save()
        return Response(
            'ok',
            status=status.HTTP_201_CREATED
        )

    def delete(self, request):
        id_image = -1
        if 'id' in request.data:
            id_image = request.data['id']
        image = get_object_or_404(Image, id=id_image)
        image.delete()
        return Response(
            'Image delete',
            status=status.HTTP_200_OK
        )

    def put(self, request):
        id_image = -1
        if 'id' in request.data:
            id_image = request.data['id']
        image = get_object_or_404(Image, id=id_image)
        image_serializer = ImageSerializer(data=request.data)
        if image_serializer.is_valid():
            image_serializer.update(image, request.data)
            return Response(
                'ok Update',
                status=status.HTTP_200_OK
            )
        return Response(
            image_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request, id):
        image = get_object_or_404(Image, id=id)
        image_serializer = ImageSerializer(
            image
        )

        return Response(
            image_serializer.data,
            status=status.HTTP_200_OK
        )

    def put_user_image(self, request, username):
        # TODO - Delete before image
        user = get_object_or_404(User, username=username)
        image_serializer = ImageSerializer(data=request.data)
        image_serializer.is_valid(raise_exception=True)
        user.image = image_serializer.save()
        user.save()
        return Response(
            'ok',
            status=status.HTTP_200_OK
        )

    def put_activity_image(self, request, activity_id):
        # TODO - verify permissions
        # TODO - Delete before image
        activity = get_object_or_404(Activity, id=activity_id)
        image_serializer = ImageSerializer(data=request.data)
        image_serializer.is_valid(raise_exception=True)
        activity.image = image_serializer.save()
        activity.save()
        return Response(
            'ok',
            status=status.HTTP_200_OK
        )

    def get_image_by_username(self, request, username):
        image = Image.objects.get(user=username)
        image_serializer = ImageSerializer(image)
        return Response(
            image_serializer.data,
            status=status.HTTP_200_OK
        )


image = ImageViewSet.as_view(dict(
    post='create'
))
