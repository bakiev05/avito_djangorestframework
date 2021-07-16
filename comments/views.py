from rest_framework import viewsets
from comments.serializers import CommentSerializer
from comments.models import Comment
from posts.models import Post


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
