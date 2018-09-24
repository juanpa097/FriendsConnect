from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .model import Rate


class RateSerializer(serializers.ModelSerializer):
    """

        This class is incharge of parse the JSON that comes
        from the API and makes it a Python Rate object.

    """
    class Meta:
        model = Rate
        fields = ('points', 'user')

    def create(self, validated_data):
        user_id = validated_data['user']
        validated_data['user'] = get_object_or_404(User, user_id=user_id)
        return Rate.objects.create(**validated_data)
