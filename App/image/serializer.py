import  base64

from rest_framework import serializers
from App.image.model import Image

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'

    def create(self, validated_data):
        return Image.objects.create(**validated_data)
