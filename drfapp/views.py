from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostListSerializer, CommentListSerializer, PostDetailSerialzier


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostDetailSerialzier
            
    
class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentListSerializer
    
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        query = Comment.objects.filter(user=post_id)
        return query