from rest_framework import serializers
from App.comment.model import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('description', 'date_created')