import base64

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from App.activity.model import Activity
from App.comment.model import Comment
from App.user.model import Profile
from App.user.serializer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(required=False)
    username = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Comment
        fields = (
            'description', 'date_created',
            'user', 'replies', 'image',
            'username'
        )

    def create(self, validated_data):
        user = validated_data.get('user', '')
        validated_data['user'] = get_object_or_404(User, id=user)
        replies = validated_data.get('replies', None)
        if replies:
            validated_data['replies'] = get_object_or_404(Comment, id=replies)
        activity = validated_data.get('activity', None)
        if activity:
            validated_data['activity'] = get_object_or_404(
                Activity,
                id=activity)
        return Comment.objects.create(**validated_data)

    def get_image(self, obj):
        try:
            profile = Profile.objects.get(user=obj.user)
        except Exception:
            profile = None
        if not profile:
            return None
        image = profile.image
        if not image:
            return None
        complete_path = image.file.path
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str

    def get_username(self, obj):
        return obj.user.username
