import base64
import os

from rest_framework import serializers

from App.image.model import Image
from .mixins import CreateImageBy64Mixin


class ImageSerializer(
    serializers.ModelSerializer,
    CreateImageBy64Mixin
):
    file = serializers.FileField(required=False, write_only=True)
    file_64 = serializers.SerializerMethodField(required=False)
    image = serializers.CharField(required=False)

    class Meta:
        model = Image
        fields = ('file', 'file_64','image')

    def create(self, validated_data):
        image = validated_data.get('image')
        if image:
            validated_data['file'] = self.getFileBy64(image)
            validated_data.pop('image')
        return Image.objects.create(**validated_data)

    def get_file_64(self, obj):
        complete_path = obj.file.path
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str

    def update(self, instance, validated_data):
        file = validated_data.get('file')
        if instance.file:
            os.remove(instance.file.path)
        if file:
            instance.file = file
        image = validated_data.get('image')
        if image:
            instance.file = self.getFileBy64(image)
        instance.save()
        return instance
