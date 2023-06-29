from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, permissions, viewsets
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

from .models import Post
from .serializers import PostSerializer, UserSerializer


# class PostList(generics.ListAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
