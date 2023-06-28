from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class Qwerty(TemplateView):
    template_name = 'index.html'

