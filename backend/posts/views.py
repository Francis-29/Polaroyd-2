from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .serializers import PostSerializer, LikeSerializer
from .models import Post, Like


class isOwner(BasePermission):
    message = 'Editing and deleting the post is restricted to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.user == request.user
    
    
class Posts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Post(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [isOwner]


class LikePost(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikePostDelete(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [isOwner]
