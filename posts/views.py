from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()



