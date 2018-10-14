from rest_framework import serializers
from App.comment.model import Comment
from App.user.serializer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('description', 'date_created', 'user', 'replies')
