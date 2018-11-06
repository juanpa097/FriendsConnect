from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from App.comment.model import Comment
from App.comment.serializer import CommentSerializer


class CommentViewSet(viewsets.ViewSet):

    def get_comments_by_comment(self, request, comment_id):
        comments = Comment.objects.filter(replies=comment_id)
        serializer = CommentSerializer(
            comments,
            many=True
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post_comments_by_comment(self, request, comment_id):
        # TODO -verify
        request.data['replies'] = comment_id
        request.data['user'] = request.user.id
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(request.data)
        return Response(
            "OK",
            status=status.HTTP_200_OK
        )

    def get_comments_by_activity(self, request, activity_id):
        comments = Comment.objects.filter(activity=activity_id)
        serializer = CommentSerializer(
            comments,
            many=True
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post_comments_by_activity(self, request, activity_id):
        # TODO -verify
        request.data['activity'] = activity_id
        request.data['user'] = request.user.id
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(request.data)
        return Response(
            "OK",
            status=status.HTTP_200_OK
        )


comments_by_comment = CommentViewSet.as_view(dict(
    post='post_comments_by_comment',
    get='get_comments_by_comment'
))
