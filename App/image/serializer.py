import base64
import os

from rest_framework import serializers

from App.image.model import Image


class ImageSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)
    file_64 = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Image
        fields = ('file', 'file_64')

    def get_file_64(self, obj):
        complete_path = obj.file.path
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str

    def update(self, instance, validated_data):
        file = validated_data.get('file')
        if file:
            os.remove(instance.file.path)
            instance.file = file
        instance.save()
        return instance
