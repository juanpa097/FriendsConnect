from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from App.activity.model import Activity
from App.comment.model import Comment
from App.user.serializer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('description', 'date_created', 'user', 'replies')

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
